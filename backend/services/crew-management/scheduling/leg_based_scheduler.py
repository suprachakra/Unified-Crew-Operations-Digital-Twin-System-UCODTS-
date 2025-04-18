"""
Leg-Based Scheduler Module
Assigns crew to individual flight legs.
"""

def assign_directly(legs: list, crew: list) -> dict:
    assignments = {}
    for i, leg in enumerate(legs):
        if i < len(crew):
            assignments[leg["id"]] = crew[i]["id"]
    return assignments
