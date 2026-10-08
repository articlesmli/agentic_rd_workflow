from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_agent_empty_payload_edge_case():
    """Test how the API handles an empty document text or missing fields."""
    # Sending an empty document_text to match ProcessRequest schema
    response = client.post("/v1/process-protocol", json={"document_text": ""})
    
    # We expect a 400 Bad Request (explicitly raised in your main.py) 
    # or a 422 Unprocessable Entity for schema validation failures.
    assert response.status_code in [400, 422]
    
    data = response.json()
    # Verify it returns a clear detail message rather than crashing
    assert "detail" in data