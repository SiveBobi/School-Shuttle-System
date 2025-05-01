from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_book():
    response = client.post("/api/books/", json={
        "book_id": "B123",
        "title": "REST in Practice",
        "author": "Sive Bobi",
        "isbn": "111222333",
        "status": "available"
    })
    assert response.status_code == 200

def test_checkout_book():
    # Assumes book B123 is already created
    response = client.post("/api/books/B123/checkout")
    assert response.status_code == 200
