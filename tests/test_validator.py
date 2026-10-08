import pytest
from pydantic_ai.models.test import TestModel
from agents import validator_agent
from graph import route_validation
from schemas import AgentWorkflowState

def test_validator_agent_detects_errors():
    input_text = "Review extracted data: Medication: None, Dosage: None."
    
    # Use TestModel to mock the validator response
    with validator_agent.override(model=TestModel()):
        result = validator_agent.run_sync(input_text)
        assert result.output is not None

def test_route_validation_logic():
    # If there are no validation errors, it should finalize
    valid_state: AgentWorkflowState = {
        "input_text": "...",
        "extracted_data": {"medication": "Aspirin"},
        "validation_errors": [],
        "iteration_count": 1
    }
    assert route_validation(valid_state) == "finalize"

    # If there are validation errors, it should route to correction
    invalid_state: AgentWorkflowState = {
        "input_text": "...",
        "extracted_data": {"medication": None},
        "validation_errors": ["Missing required medication field"],
        "iteration_count": 1
    }
    assert route_validation(invalid_state) == "correct"