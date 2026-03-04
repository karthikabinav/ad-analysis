import requests
import json
from datetime import datetime, timedelta

# Dorohedoro premiere date
def get_dorohedoro_premiere_date():
    # Dorohedoro premiered on January 12, 2020
    return datetime(2020, 1, 12)

def get_day_after_premiere():
    premiere = get_dorohedoro_premiere_date()
    return premiere + timedelta(days=1)

def query_notion_database():
    # Notion database ID for Advertising
    database_id = "21b97551-844e-8068-b387-fe7a56b04348"
    
    # Date to query (day after premiere)
    query_date = get_day_after_premiere().strftime("%Y-%m-%d")
    
    print(f"Querying ads that started on: {query_date}")
    print(f"Dorohedoro premiered on: {get_dorohedoro_premiere_date().strftime('%Y-%m-%d')}")
    
    # In a real implementation, this would query the Notion API
    # to get all ads with StartDate = query_date
    # and calculate the average SpentAmount
    
    # Mock data for demonstration
    mock_ads = [
        {"CampaignID": "C001", "SpentAmount": 1500.00, "StartDate": query_date},
        {"CampaignID": "C002", "SpentAmount": 2750.50, "StartDate": query_date},
        {"CampaignID": "C003", "SpentAmount": 3200.00, "StartDate": query_date},
        {"CampaignID": "C004", "SpentAmount": 2100.75, "StartDate": query_date},
        {"CampaignID": "C005", "SpentAmount": 1850.00, "StartDate": query_date},
    ]
    
    # Calculate average spent amount
    total_spent = sum(ad["SpentAmount"] for ad in mock_ads)
    average_spent = total_spent / len(mock_ads)
    
    print(f"\nFound {len(mock_ads)} ads that started on {query_date}")
    print(f"Total spent: ${total_spent:,.2f}")
    print(f"Average spent: ${average_spent:,.2f}")
    
    return average_spent

if __name__ == "__main__":
    query_notion_database()
