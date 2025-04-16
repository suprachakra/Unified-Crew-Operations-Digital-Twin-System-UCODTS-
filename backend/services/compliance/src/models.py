"""
Models for regulatory rules and compliance violations.
Ensures data integrity and provides JSON schema definitions.
"""

from pydantic import BaseModel
from datetime import datetime

class RegulatoryRule(BaseModel):
    region: str
    max_duty_hours: int
    min_rest_hours: int

class ComplianceViolation(BaseModel):
    crew_id: int
    rule: str
    description: str
    timestamp: datetime