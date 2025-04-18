"""
Alerts Controller.
Generates alerts for significant deviations or emergencies.
"""

import logging

def generate_alert(flight: dict) -> dict:
    try:
        alert_msg = f"Deviation detected for flight {flight.get('id')}!"
        logging.warning(alert_msg)
        return {"flight_id": flight.get("id"), "alert": alert_msg}
    except Exception as e:
        logging.error("Error generating alert: %s", e)
        return {"error": "Alert generation failed."}
