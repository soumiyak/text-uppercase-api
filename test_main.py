from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_uppercase():
    response = client.post("/uppercase", json={"text": "hello"})
    assert response.status_code == 200
    assert response.json() == {"result": "HELLO"}
