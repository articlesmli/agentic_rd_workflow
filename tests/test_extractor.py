from pydantic_ai.models.test import TestModel

from agents import extractor_agent


def test_extractor_agent_basic():
    input_prompt = "Extract protocol details: Patient received 10mg of medication X daily for 5 days."
    
    # Use TestModel to mock the agent response
    with extractor_agent.override(model=TestModel()):
        result = extractor_agent.run_sync(input_prompt)
        
        # Verify output was successfully structured
        assert result.output is not None