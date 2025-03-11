# Common Utility Functions

def format_date(date_obj):
    """Format a date object to YYYY-MM-DD string."""
    return date_obj.strftime("%Y-%m-%d")

def calculate_fatigue_score(schedule_data):
    """Calculate a simple fatigue score based on provided schedule data.
    
    Args:
        schedule_data (list): List of numerical schedule metrics.
    
    Returns:
        float: Average fatigue score.
    """
    if not schedule_data:
        return 0.0
    return sum(schedule_data) / len(schedule_data)
