"""
Satcom Connector.
Simulates satellite communications data for flight tracking.
"""

def get_satcom_data(flight_id: int) -> dict:
    try:
        return {"flight_id": flight_id, "data": "Simulated satcom data."}
    except Exception:
        return {"error": "Satellite data fetch failed."}
