"""
Schedule Evaluator Module
Provides metrics to assess the quality of the generated crew schedule.
"""

def evaluate_schedule(schedule: dict) -> dict:
    quality_score = len(schedule.get("assignments", {}))
    return {"quality_score": quality_score}
