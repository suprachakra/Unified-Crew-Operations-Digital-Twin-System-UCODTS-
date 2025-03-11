# Flight Service API Endpoints

from fastapi import APIRouter
from .models import Flight
from datetime import datetime

router = APIRouter()

# Dummy flight data for demonstration purposes
flights = [
    {
        "flight_id": 1,
        "flight_number": "EK101",
        "departure": "DXB",
        "arrival": "LHR",
        "scheduled_departure": datetime(2023, 12, 1, 9, 0),
        "scheduled_arrival": datetime(2023, 12, 1, 14, 0),
        "status": "On-Time",
        "delay_reason": ""
    },
    {
        "flight_id": 2,
        "flight_number": "EK102",
        "departure": "LHR",
        "arrival": "JFK",
        "scheduled_departure": datetime(2023, 12, 2, 10, 0),
        "scheduled_arrival": datetime(2023, 12, 2, 15, 0),
        "status": "Delayed",
        "delay_reason": "Weather conditions"
    }
    # ... (assume more records)
]

@router.get("/list", response_model=list[Flight])
async def get_flights():
    return flights
