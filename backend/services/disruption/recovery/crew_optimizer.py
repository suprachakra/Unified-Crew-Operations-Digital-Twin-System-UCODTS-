"""
Crew Optimizer Module
Implements AI-driven crew reassignment logic.
"""

import logging

def optimize_crew_assignment(disrupted_flight: dict, available_crew: list) -> dict:
    try:
        if not available_crew:
            logging.warning("No available crew found for flight %s", disrupted_flight.get("id"))
            return {"error": "No available crew found."}
        # Dummy logic: choose the crew with lowest current duty hours.
        available = sorted(available_crew, key=lambda c: float(c.get("duty_hours", 0)))
        selected = available[0]
        logging.info("Optimized assignment for flight %s: new crew %s", disrupted_flight.get("id"), selected.get("id"))
        return {"flight_id": disrupted_flight.get("id"), "new_crew_id": selected.get("id")}
    except Exception as e:
        logging.error("Error in crew optimizer: %s", e)
        return {"error": "Optimizer error"}
