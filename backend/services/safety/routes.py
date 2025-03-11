# Safety Service API Endpoints

from fastapi import APIRouter
from .models import SafetyIncident

router = APIRouter()

# Dummy safety incidents data for demonstration purposes
incidents = [
    {
        "incident_id": 1,
        "flight_id": 1,
        "incident_type": "System Failure",
        "severity": "High",
        "incident_time": "2023-11-20T12:30:00",
        "resolution": "Immediate maintenance performed."
    },
    {
        "incident_id": 2,
        "flight_id": 2,
        "incident_type": "Minor Fault",
        "severity": "Low",
        "incident_time": "2023-11-21T09:15:00",
        "resolution": "Fault logged for review."
    }
    # ... (assume more records)
]

@router.get("/list", response_model=list[SafetyIncident])
async def get_safety_incidents():
    return incidents
