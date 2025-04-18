"""
Duty Impact Calculator Module
Evaluates the impact of schedule changes on crew fatigue.
"""

import logging

def calculate_duty_impact(schedule_change: dict) -> float:
    try:
        extra_hours = float(schedule_change.get("extra_hours", 0))
        impact = min(1.0, extra_hours / 10.0)
        logging.info("Calculated duty impact: extra_hours=%s, impact=%s", extra_hours, impact)
        return round(impact, 2)
    except Exception as e:
        logging.error("Error calculating duty impact: %s", e)
        return 0.0
