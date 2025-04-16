"""
FTL Calculator – checks if crew duty hours exceed regulatory limits.
This module contains risk mitigation by logging and returning detailed messages.
"""

import logging

def check_ftl(schedule: dict) -> list:
    """
    Check Flight Time Limitations.
    Returns a list of violation messages if any crew member exceeds allowed duty hours.
    """
    violations = []
    try:
        for crew in schedule.get("crew", []):
            duty_hours = float(crew.get("duty_hours", 0))
            # Example threshold, can be extended per region.
            if duty_hours > 14:
                msg = f"Crew {crew.get('id')} exceeds duty hours: {duty_hours} > 14."
                logging.info("FTL violation: %s", msg)
                violations.append(msg)
    except Exception as e:
        logging.error("Error in FTL calculation: %s", e)
        violations.append("Error in FTL calculation.")
    return violations