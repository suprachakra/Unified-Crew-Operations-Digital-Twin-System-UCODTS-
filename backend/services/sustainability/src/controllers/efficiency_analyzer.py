"""
Efficiency Analyzer Module
Computes fuel efficiency metrics.
"""

def analyze_efficiency(flight: dict) -> dict:
    try:
        distance = float(flight.get("distance", 0))
        fuel_used = float(flight.get("fuel_used", 1))  # Avoid division by zero.
        efficiency = distance / fuel_used
        return {"flight_id": flight.get("id"), "fuel_efficiency": round(efficiency, 2)}
    except Exception:
        return {"error": "Efficiency analysis error"}
