"""
Mitigation Recommender Module
Suggests countermeasures based on crew alertness levels.
"""

import logging

def recommend_mitigation(alertness_score: float) -> str:
    try:
        if alertness_score < 0.5:
            recommendation = "Recommend extended rest period and caffeine intake."
        elif alertness_score < 0.7:
            recommendation = "Suggest a short break and monitoring."
        else:
            recommendation = "No additional measures necessary."
        logging.info("Mitigation recommendation for score %s: %s", alertness_score, recommendation)
        return recommendation
    except Exception as e:
        logging.error("Error computing mitigation recommendation: %s", e)
        return "Consult manual intervention."
