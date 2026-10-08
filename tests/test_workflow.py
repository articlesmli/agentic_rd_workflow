# test_workflow.py
from fastapi.testclient import TestClient

from main import app
from schemas import ProtocolExtraction

client = TestClient(app)

def test_health_check_or_empty_document():
    # Test that sending an empty document properly raises a 400 Bad Request
    response = client.post("/v1/process-protocol", json={"document_text": "   "})
    assert response.status_code == 400
    assert response.json()["detail"] == "Document text cannot be empty."

def test_protocol_extraction_schema():
    # Test that our Pydantic schema validates correctly
    data = {
        "phase": "Phase II",
        "primary_endpoint": "Safety and efficacy",
        "inclusion_criteria": ["Adults over 18"],
        "exclusion_criteria": ["Pregnant women"],
        "sample_size": 100
    }
    extraction = ProtocolExtraction(**data)
    assert extraction.phase == "Phase II"
    assert extraction.sample_size == 100
