"""
Audit Trail Utility – logs compliance audits for traceability.
Designed with risk mitigation in mind (persisting logs, error checking).
"""

import logging
from datetime import datetime

logger = logging.getLogger("compliance_audit")
logger.setLevel(logging.INFO)

def log_audit(crew_id: int, rule: str, description: str):
    try:
        timestamp = datetime.utcnow().isoformat()
        log_message = f"{timestamp} - Crew {crew_id} violated {rule}: {description}"
        logger.info(log_message)
        # In a production system, this should be written to a durable store.
    except Exception as e:
        logger.error("Failed to log audit for crew %s: %s", crew_id, e)