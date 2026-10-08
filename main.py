from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from graph import compiled_graph
from schemas import AgentWorkflowState, ProtocolExtraction, ValidationReport

app = FastAPI(title="Agentic R&D Workflow API")

class ProcessRequest(BaseModel):
    document_text: str
    max_validation_attempts: int = 3

class ProcessResponse(BaseModel):
    status: str
    iterations_run: int
    extracted_data: ProtocolExtraction
    validation_summary: ValidationReport

@app.post("/v1/process-protocol", response_model=ProcessResponse)
async def process_rd_document(request: ProcessRequest):
    if not request.document_text.strip():
        raise HTTPException(status_code=400, detail="Document text cannot be empty.")

    # Initialize graph state
    initial_state = AgentWorkflowState(
        raw_document=request.document_text,
        max_loops=request.max_validation_attempts
    )
    
    try:
        # Execute the state graph asynchronously
        final_state_dict = await compiled_graph.ainvoke(initial_state)
        
        return ProcessResponse(
            status="success" if final_state_dict["validation_report"].is_valid else "max_loops_exceeded_with_warnings",
            iterations_run=final_state_dict["loop_count"],
            extracted_data=final_state_dict["extracted_data"],
            validation_summary=final_state_dict["validation_report"]
        )

    except Exception as e:  # noqa: BLE001
        # Log error to telemetry system here
        raise HTTPException(status_code=500, detail=f"Graph runtime exception: {e!s}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
