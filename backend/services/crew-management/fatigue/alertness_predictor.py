"""
Alertness Predictor Module
Combines biometric data with circadian models to provide a crew alertness score.
"""

from .biometric_integration import fetch_biometric_data
from .circadian_model import predict_alertness
import logging

def predict_crew_alertness(crew_id: int, current_hour: int) -> float:
    try:
        biometrics = fetch_biometric_data(crew_id)
        base_alert = predict_alertness(current_hour)
        sleep_quality = biometrics.get("sleep_quality", 0.5)
        combined = (base_alert + sleep_quality) / 2
        score = round(combined, 2)
        logging.info("Predicted alertness for crew %s at hour %s: %s", crew_id, current_hour, score)
        return score
    except Exception as e:
        logging.error("Error predicting alertness for crew %s: %s", crew_id, e)
        return 0.5
