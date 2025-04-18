"""
Preferential Bidding Module
Handles crew bidding preferences for flight assignments.
"""

def process_crew_bids(bids: list) -> dict:
    if not bids:
        return {}
    winning_bid = max(bids, key=lambda bid: bid.get("bid_value", 0))
    return {"assigned_bid": winning_bid}
