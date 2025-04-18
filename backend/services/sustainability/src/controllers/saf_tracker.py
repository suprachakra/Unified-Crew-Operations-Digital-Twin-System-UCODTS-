"""
SAF Tracker Module
Estimates usage of Sustainable Aviation Fuel (SAF).
"""

def track_saf_usage(flight: dict) -> dict:
    try:
        fuel_used = float(flight.get("fuel_used", 0))
        saf_amount = fuel_used * 0.05  # Assume 5% usage for demonstration.
        return {"flight_id": flight.get("id"), "saf_used": saf_amount}
    except Exception:
        return {"error": "SAF tracking error"}
