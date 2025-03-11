# Disruption Service API Endpoints

from fastapi import APIRouter
from .models import DisruptionEvent

router = APIRouter()

# Dummy data for disruption events
disruptions = [
    {
        "disruption_id": 1,
        "flight_id": 1,
        "type": "Weather",
        "description": "Heavy rain causing flight delays.",
        "detected_time": "2023-11-25T08:00:00"
    },
    {
        "disruption_id": 2,
        "flight_id": 2,
        "type": "Geopolitical",
        "description": "Airspace restrictions due to regional conflict.",
        "detected_time": "2023-11-26T09:30:00"
    }
    # ... (assume more records)
]

@router.get("/list", response_model=list[DisruptionEvent])
async def get_disruptions():
    return disruptions
