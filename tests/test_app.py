import json
from app.main import app

client = app.test_client()

def test_health():
    response = client.get("/")
    assert response.status_code == 200

def test_get_students():
    response = client.get("/students")
    assert response.status_code == 200

def test_add_student():
    response = client.post("/students", json={"name": "Alice", "age": 21})
    assert response.status_code == 201

def test_delete_student():
    client.post("/students", json={"name": "Charlie", "age": 20})
    response = client.delete("/students/0")
    assert response.status_code == 200
