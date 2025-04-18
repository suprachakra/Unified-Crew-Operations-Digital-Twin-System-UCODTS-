"""
Compliance Monitoring Module
Periodically checks active schedules to detect potential violations.
"""

import time
import logging
from controllers import ftl_calculator, rest_requirements

def monitor_compliance(schedule: dict, interval: int = 300):
    """
    Periodically checks the schedule every 'interval' seconds.
    Logs any potential violations.
    """
    while True:
        try:
            violations = []
            violations.extend(ftl_calculator.check_ftl(schedule))
            violations.extend(rest_requirements.check_rest(schedule))
            if violations:
                logging.warning("Compliance monitoring detected violations: %s", violations)
            else:
                logging.info("Compliance monitoring: No violations detected.")
        except Exception as e:
            logging.error("Error in compliance monitoring loop: %s", e)
        time.sleep(interval)
