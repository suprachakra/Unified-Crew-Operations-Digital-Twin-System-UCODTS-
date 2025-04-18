"""
Standby Allocation Module
Determines which crew members should be allocated as standby.
"""

import logging

def allocate_standby(crew_list: list) -> list:
    try:
        # Dummy logic: select the two crew with the lowest duty hours.
        sorted_crew = sorted(crew_list, key=lambda c: float(c.get("duty_hours", 0)))
        standby = sorted_crew[:2]
        logging.info("Allocated standby crew: %s", [c.get("id") for c in standby])
        return standby
    except Exception as e:
        logging.error("Error allocating standby crew: %s", e)
        return []
