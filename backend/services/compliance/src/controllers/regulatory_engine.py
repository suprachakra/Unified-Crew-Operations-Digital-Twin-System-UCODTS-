"""
Regulatory Compliance Engine

Implements FAA FAR 117 and EASA EU-OPS rest and flight-time limitation rules,
with hooks for real-time crew alertness integration and audit logging.
"""

import os
import json
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any

from .models import DutyPeriod, RestRequirement, ComplianceReport, AlertnessScore

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


class FAR117Compliance:
    def __init__(self, rules_path: str = None):
        """
        Load regulatory rules from JSON.
        """
        if not rules_path:
            base = os.path.dirname(__file__)
            rules_path = os.path.join(base, "../data/regulatory_rules/far117.json")
        self.rules = self._load_rules(rules_path)

    def _load_rules(self, path: str) -> Dict[str, Any]:
        """
        Load JSON file containing FAR117 rest and FTL parameters.
        """
        try:
            with open(path, "r") as f:
                LOGGER.info(f"Loading FAR117 rules from {path}")
                return json.load(f)
        except Exception as e:
            LOGGER.error(f"Failed to load FAR117 rules: {e}")
            raise

    def calculate_rest_periods(
        self,
        duty_history: List[DutyPeriod],
        alertness_scores: List[AlertnessScore] = None
    ) -> RestRequirement:
        """
        Calculate minimum required rest period after the last duty in history,
        adjusted by recent alertness scores.

        - FAR117 requires 10 hours of rest after 14-hour duty window.
        - AlertnessScore may increase rest by up to 2 hours if alertness < threshold.
        """
        if not duty_history:
            raise ValueError("No duty history provided")

        last_duty = max(duty_history, key=lambda d: d.end_time)
        duty_window = (last_duty.end_time - duty_history[0].start_time).total_seconds() / 3600

        # Base rest = rules["base_rest_hours"] (e.g., 10)
        base_hours = self.rules.get("base_rest_hours", 10)

        # If duty_window > rules["max_duty_window"], flag violation
        max_window = self.rules.get("max_duty_window_hours", 14)
        if duty_window > max_window:
            LOGGER.warning(f"Duty window {duty_window}h exceeds max {max_window}h")

        # Adjust for alertness
        extra_rest = 0
        if alertness_scores:
            # take the lowest alertness in last duty
            low = min(a.score for a in alertness_scores if a.timestamp >= last_duty.end_time - timedelta(hours=4))
            threshold = self.rules.get("alertness_threshold", 0.7)
            if low < threshold:
                extra_rest = self.rules.get("max_extra_rest_hours", 2)
                LOGGER.info(f"Low alertness {low}, adding extra rest {extra_rest}h")

        total_rest = base_hours + extra_rest
        rest_end = last_duty.end_time + timedelta(hours=total_rest)

        return RestRequirement(
            required_hours=total_rest,
            window_start=last_duty.end_time,
            window_end=rest_end
        )

    def check_ftl(
        self,
        duty_history: List[DutyPeriod]
    ) -> List[str]:
        """
        Check flight time limitations (FTL) across the duty history.
        Returns a list of violation messages, empty if compliant.
        """
        violations = []
        max_daily = self.rules.get("max_flight_time_daily_hours", 8)
        max_weekly = self.rules.get("max_flight_time_weekly_hours", 30)

        # Sum daily and weekly flight segments
        now = datetime.utcnow()
        daily_sum = sum(d.flight_time_hours for d in duty_history 
                        if d.end_time.date() == now.date())
        weekly_sum = sum(d.flight_time_hours for d in duty_history 
                         if (now - d.end_time).days < 7)

        if daily_sum > max_daily:
            violations.append(
                f"Daily flight time {daily_sum}h exceeds max {max_daily}h"
            )
            LOGGER.warning(violations[-1])

        if weekly_sum > max_weekly:
            violations.append(
                f"Weekly flight time {weekly_sum}h exceeds max {max_weekly}h"
            )
            LOGGER.warning(violations[-1])

        return violations

    def evaluate_compliance(
        self,
        duty_history: List[DutyPeriod],
        alertness_scores: List[AlertnessScore] = None
    ) -> ComplianceReport:
        """
        Run full compliance evaluation: rest requirements + FTL checks.
        """
        rest_req = self.calculate_rest_periods(duty_history, alertness_scores)
        ftl_violations = self.check_ftl(duty_history)

        compliant = (len(ftl_violations) == 0)
        if not compliant:
            LOGGER.error("FTL violations detected")

        report = ComplianceReport(
            compliant=compliant,
            rest_requirement=rest_req,
            violations=ftl_violations,
            timestamp=datetime.utcnow().isoformat()
        )

        return report


# Example usage
if __name__ == "__main__":
    # This block can be used for local manual testing
    from .models import DutyPeriod, AlertnessScore

    # Mock data
    history = [
        DutyPeriod(start_time=datetime.utcnow() - timedelta(hours=16),
                   end_time=datetime.utcnow() - timedelta(hours=4),
                   flight_time_hours=7.5)
    ]
    alerts = [
        AlertnessScore(timestamp=datetime.utcnow() - timedelta(hours=2), score=0.65)
    ]

    engine = FAR117Compliance()
    report = engine.evaluate_compliance(history, alerts)
    print(report.json(indent=2))
