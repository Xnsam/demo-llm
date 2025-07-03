from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the LLM API"}

def test_generate():
    response = client.post("/generate", json={"text": "once upon a time"})
    assert response.status_code == 200
    assert "generated_text" in response.json()

