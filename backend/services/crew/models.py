# Crew Service Data Models

from pydantic import BaseModel
from datetime import date

class CrewMember(BaseModel):
    crew_id: int
    name: str
    role: str
    fatigue_score: float
    last_scheduled: date
