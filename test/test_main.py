import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_query_endpoint():
    response = client.post("/query", json={"query": "Hello"})
    assert response.status_code == 200
    assert "message" in response.json()

def test_summarize_endpoint():
    long_text = "This is a long text input that should be summarized. " * 10
    response = client.post("/summarize", json={"text": long_text})
    assert response.status_code == 200
    assert "summary" in response.json()

def test_summarize_short_text():
    response = client.post("/summarize", json={"text": "Short"})
    assert response.status_code == 400  # Should fail due to short input
