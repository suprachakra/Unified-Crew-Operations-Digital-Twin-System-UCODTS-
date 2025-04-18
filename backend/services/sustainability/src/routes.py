"""
API routes for Sustainability Tracking Service.
"""

from fastapi import APIRouter, HTTPException
from controllers import carbon_calculator, saf_tracker, efficiency_analyzer
import logging

router = APIRouter()

@router.post("/calculate")
async def calculate_emission(flight: dict):
    try:
        result = carbon_calculator.calculate_emissions(flight)
        logging.info("Emissions calculated for flight %s", flight.get("id"))
        return result
    except Exception as e:
        logging.error("Error calculating emissions: %s", e)
        raise HTTPException(status_code=500, detail="Emissions calculation failed.")

@router.get("/summary")
async def summary():
    try:
        # Return a dummy summary; integrate with database aggregation in production.
        summary_data = {"total_co2": 12345.6, "average_per_flight": 250.5}
        logging.info("Sustainability summary provided.")
        return summary_data
    except Exception as e:
        logging.error("Error fetching sustainability summary: %s", e)
        raise HTTPException(status_code=500, detail="Sustainability summary failed.")
