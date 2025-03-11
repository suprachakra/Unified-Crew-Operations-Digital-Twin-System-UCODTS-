# Maintenance Service API Endpoints

from fastapi import APIRouter
from .models import MaintenanceEvent

router = APIRouter()

# Dummy data for demonstration purposes
maintenance_events = [
    {
        "maintenance_id": 1,
        "flight_id": 1,
        "equipment": "Engine",
        "maintenance_date": "2023-11-15",
        "status": "Pending",
        "description": "Engine diagnostic test pending."
    },
    {
        "maintenance_id": 2,
        "flight_id": 2,
        "equipment": "Avionics",
        "maintenance_date": "2023-11-16",
        "status": "Completed",
        "description": "Routine avionics inspection completed."
    }
    # ... (assume more records)
]

@router.get("/list", response_model=list[MaintenanceEvent])
async def get_maintenance_events():
    return maintenance_events
