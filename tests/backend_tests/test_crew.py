import pytest
from fastapi.testclient import TestClient
from services.crew.service import app

client = TestClient(app)

def test_crew_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "Crew service is operational"}

def test_get_crew_list():
    response = client.get("/api/v1/crew/list")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    # Verify that the list contains 50 crew members if using dummy data
    assert len(data) >= 1  # Adjust as per your dummy data
