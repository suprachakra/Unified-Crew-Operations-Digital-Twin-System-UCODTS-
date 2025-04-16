"""
API routes for the Regulatory Compliance Service.
Provides the /validate endpoint.
"""

from fastapi import APIRouter, HTTPException
from controllers import ftl_calculator, rest_requirements, rule_engine
import logging

router = APIRouter()

@router.post("/validate")
async def validate_schedule(schedule: dict):
    """
    Validate the provided crew schedule.
    Expects a JSON object with schedule details.
    Returns status OK if compliant; otherwise, raises HTTPException with a list of violations.
    """
    logging.info("Validating schedule: %s", schedule)
    try:
        violations = []
        violations.extend(ftl_calculator.check_ftl(schedule))
        violations.extend(rest_requirements.check_rest(schedule))
        violations.extend(rule_engine.apply_rules(schedule))
        if violations:
            logging.warning("Schedule violations detected: %s", violations)
            raise HTTPException(status_code=400, detail={"violations": violations})
        logging.info("Schedule is compliant")
        return {"status": "OK", "message": "Schedule compliant."}
    except Exception as e:
        logging.error("Error while validating schedule: %s", e)
        raise HTTPException(status_code=500, detail="Internal server error during compliance validation.")