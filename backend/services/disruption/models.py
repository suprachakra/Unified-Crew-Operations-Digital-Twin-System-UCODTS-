# models.py - Disruption Service Data Models

from pydantic import BaseModel
from datetime import datetime

class DisruptionEvent(BaseModel):
    disruption_id: int
    flight_id: int
    type: str
    description: str
    detected_time: datetime
