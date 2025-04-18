"""
Carbon Calculator Module
Calculates emissions using a fixed factor.
"""

def calculate_emissions(flight: dict) -> dict:
    try:
        fuel_used = float(flight.get("fuel_used", 0))
        # Example: 3.15 kg CO₂ per kg of fuel.
        co2 = fuel_used * 3.15
        return {"flight_id": flight.get("id"), "fuel_used": fuel_used, "co2_emitted": co2}
    except Exception as e:
        return {"error": "Emission calculation error"}
