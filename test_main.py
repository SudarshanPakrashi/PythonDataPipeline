from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

def test_read_main():
    response = client.get("/search/Barack")
    assert response.status_code == 200

def test_read_main():
    response = client.get("/wiki/Barack Obama/10")
    assert response.status_code == 200
