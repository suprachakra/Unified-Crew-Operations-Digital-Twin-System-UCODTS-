# Flight Service Data Models

from pydantic import BaseModel
from datetime import datetime

class Flight(BaseModel):
    flight_id: int
    flight_number: str
    departure: str
    arrival: str
    scheduled_departure: datetime
    scheduled_arrival: datetime
    status: str
    delay_reason: str = None
