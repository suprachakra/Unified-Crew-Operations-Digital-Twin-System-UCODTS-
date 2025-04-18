"""
ADS-B Connector.
Simulates connection to an ADS-B data source for real-time flight positions.
"""

def get_adsb_data(flight_id: int) -> dict:
    try:
        return {"flight_id": flight_id, "data": "Simulated ADS-B data."}
    except Exception:
        return {"error": "ADS-B data fetch failed."}
