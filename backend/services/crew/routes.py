# Crew Service API Endpoints

from fastapi import APIRouter
from .models import CrewMember

router = APIRouter()

# Dummy data for demonstration purposes
crew_members = [
    {"crew_id": 1, "name": "Crew Member 1", "role": "Pilot", "fatigue_score": 0.45, "last_scheduled": "2023-11-01"},
    {"crew_id": 2, "name": "Crew Member 2", "role": "Attendant", "fatigue_score": 0.48, "last_scheduled": "2023-11-02"}
    # ... (assume more records)
]

@router.get("/list", response_model=list[CrewMember])
async def get_crew():
    return crew_members
