"""
API routes for Digital Twin Synchronization.
"""

from fastapi import APIRouter
from controllers import physical_to_digital, digital_to_physical, simulation_engine
import logging

router = APIRouter()

@router.post("/update_physical")
async def update_physical(sync_data: dict):
    try:
        result = physical_to_digital.sync_update(sync_data)
        logging.info("Physical to digital sync completed for asset %s", sync_data.get("asset_id"))
        return result
    except Exception as e:
        logging.error("Error in physical_to_digital sync: %s", e)
        return {"error": "Sync failed."}

@router.post("/update_digital")
async def update_digital(sync_data: dict):
    try:
        result = digital_to_physical.sync_update(sync_data)
        logging.info("Digital to physical sync command sent for asset %s", sync_data.get("asset_id"))
        return result
    except Exception as e:
        logging.error("Error in digital_to_physical sync: %s", e)
        return {"error": "Sync failed."}

@router.get("/simulate")
async def run_simulation():
    try:
        result = simulation_engine.run_simulation()
        logging.info("Simulation executed successfully.")
        return result
    except Exception as e:
        logging.error("Error in simulation: %s", e)
        return {"error": "Simulation failed."}
