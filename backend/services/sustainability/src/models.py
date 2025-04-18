"""
Data models for Sustainability Tracking.
"""

from pydantic import BaseModel
from datetime import date

class FlightEmission(BaseModel):
    flight_id: int
    fuel_used: float  # kg of fuel used
    co2_emitted: float  # kg of CO₂ emitted
    date: date
