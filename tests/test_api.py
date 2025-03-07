from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_query_endpoint():
    response = client.post("/query", json={"query": "Hello"})
    assert response.status_code == 200
    assert "message" in response.json()

def test_summarize_endpoint():
    response = client.post("/summarize", json={"text": "Long-form text content for summarization..."})
    assert response.status_code == 200
    assert "summary" in response.json()
