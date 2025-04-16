"""
Rest Requirements Calculator – validates that minimum rest periods are observed.
Includes logging for traceability.
"""

import logging

def check_rest(schedule: dict) -> list:
    """
    Check rest period requirements for all crew members.
    Returns a list of violations if any crew gets less than the minimum rest hours.
    """
    violations = []
    try:
        for crew in schedule.get("crew", []):
            rest_hours = float(crew.get("rest_hours", 0))
            if rest_hours < 10:  # Example rule: minimum 10 hours
                msg = f"Crew {crew.get('id')} has insufficient rest: {rest_hours} < 10."
                logging.info("Rest violation: %s", msg)
                violations.append(msg)
    except Exception as e:
        logging.error("Error in rest requirements check: %s", e)
        violations.append("Error in rest requirements calculation.")
    return violations