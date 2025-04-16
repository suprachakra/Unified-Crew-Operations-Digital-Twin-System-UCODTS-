"""
Rule Engine – applies additional custom rules for schedule validation.
Logs potential risks and applies business rules consistently.
"""

import logging

def apply_rules(schedule: dict) -> list:
    """
    Apply custom scheduling rules.
    Example: Check for duplicate crew assignments.
    Returns a list of violation messages.
    """
    violations = []
    try:
        crew_ids = [crew.get("id") for crew in schedule.get("crew", [])]
        if len(crew_ids) != len(set(crew_ids)):
            msg = "Duplicate crew assignment found."
            logging.warning("Rule violation: %s", msg)
            violations.append(msg)
    except Exception as e:
        logging.error("Error in custom rule engine: %s", e)
        violations.append("Error in applying custom rules.")
    return violations