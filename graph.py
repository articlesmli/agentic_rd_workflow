from typing import Literal

from langgraph.graph import END, StateGraph

from agents import extractor_agent, validator_agent
from schemas import AgentWorkflowState


# Node 1: Extract/Correct Data
async def extract_protocol_node(state: AgentWorkflowState) -> dict:
    prompt = f"Document:\n{state.raw_document}"
    
    # If this is a cyclical loop iteration, pass the correction context
    if state.validation_report and not state.validation_report.is_valid:
        prompt += (
            f"\n\nPrevious Attempted Extraction: {state.extracted_data.model_dump_json()}\n"
            f"Validation Errors Found: {state.validation_report.issues}\n"
            f"Correction Guidance: {state.validation_report.recommended_fixes}"
        )
        
    result = await extractor_agent.run(prompt)
    
    return {
        "extracted_data": result.data,
        "loop_count": state.loop_count + 1
    }

# Node 2: Validate Data
async def validate_protocol_node(state: AgentWorkflowState) -> dict:
    prompt = (
        f"Verify this structured data for internal contradictions:\n"
        f"{state.extracted_data.model_dump_json()}"
    )
    result = await validator_agent.run(prompt)
    return {"validation_report": result.data}

# Conditional Routing Logic
def route_validation(state: AgentWorkflowState) -> Literal["correct", "finalize"]:
    # Use dictionary bracket notation safely
    report = state.get("validation_report")
    
    # Check if report exists and is valid, or fallback to checking errors list
    if report and getattr(report, "is_valid", False):
        return "finalize"
    
    # Alternatively, if your graph relies on validation_errors list:
    errors = state.get("validation_errors", [])
    if not errors:
        return "finalize"
        
    return "correct"

# Build the Graph
workflow = StateGraph(AgentWorkflowState)

# Add Nodes
workflow.add_node("extract_data", extract_protocol_node)
workflow.add_node("validate_data", validate_protocol_node)

# Set Entry Point
workflow.set_entry_point("extract_data")

# Linear Edge
workflow.add_edge("extract_data", "validate_data")

# Cyclical/Conditional Loop Edge
workflow.add_conditional_edges(
    "validate_data",
    route_validation,
    {
        "correct": "extract_data",   # The Loopback
        "finalize": END              # The Exit
    }
)

# Compile Graph
compiled_graph = workflow.compile()
