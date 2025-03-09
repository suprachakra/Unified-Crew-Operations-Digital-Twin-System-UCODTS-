import pytest
from fastapi.testclient import TestClient
from services.auth.app import app

client = TestClient(app)

def test_health():
    response = client.get("/api/v1/auth/health")
    assert response.status_code == 200
    assert response.json() == {"status": "Auth service is operational"}

def test_login_success():
    payload = {"username": "user@example.com", "password": "securePassword"}
    response = client.post("/api/v1/auth/login", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "token" in data

def test_login_failure():
    payload = {"username": "user@example.com", "password": "wrongPassword"}
    response = client.post("/api/v1/auth/login", json=payload)
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"
