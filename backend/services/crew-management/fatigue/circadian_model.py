"""
Circadian Model Module
Provides a simple model to predict alertness based on time of day.
"""

import math
import logging

def predict_alertness(hour: int) -> float:
    try:
        # Simple sine-wave model: peaks around noon.
        alertness = 0.5 + 0.5 * math.sin((hour - 6) * (3.14159 / 12))
        logging.debug("Predicted alertness at hour %s: %s", hour, alertness)
        return alertness
    except Exception as e:
        logging.error("Error in circadian model at hour %s: %s", hour, e)
        return 0.5
