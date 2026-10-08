# agents.py
from pydantic_ai import Agent

from schemas import ProtocolExtraction, ValidationReport

# Agent 1: The Domain Expert Extractor
extractor_agent = Agent(
    'anthropic:claude-3-5-sonnet-20241022',
    output_type=ProtocolExtraction,
    system_prompt=(
        "You are an expert clinical trial data extractor. Parse the provided R&D document "
        "and isolate key protocol metrics precisely. If feedback is provided from a validation "
        "failure, correct your previous extraction accordingly."
    )
)

# Agent 2: The Medical Validator
validator_agent = Agent(
    'anthropic:claude-3-5-sonnet-20241022',
    output_type=ValidationReport,
    system_prompt=(
        "You are a clinical trials QA auditor. Review the extracted structured data against "
        "medical logic. For example: Ensure exclusion criteria do not directly contradict inclusion "
        "criteria, and verify that sample sizes align with the stated trial phase standards. "
        "Flag all inconsistencies clearly."
    )
)

