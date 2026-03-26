import random
import requests
from datetime import date, timedelta

def seed_data():
    hotel_names = [
        "Grand Plaza Hotel", "Ocean View Resort", "Mountain Retreat", 
        "Urban Oasis", "The Ritz Carlton", "Hilton Garden Inn", 
        "Marriott Riverside", "Sunset Boutique Hotel", "Crystal Palace", 
        "Emerald Suites", "Sapphire Sands", "The Continental", 
        "Metropolitan Inn", "Regency Park", "Heritage Lodge"
    ]

    base_url = "https://web-production-a30b6.up.railway.app/api"
    hotels_url = f"{base_url}/hotels/"

    print(f"Adding {len(hotel_names)} hotels via POST...")
    for name in hotel_names:
        response = requests.post(hotels_url, json={"name": name})
        if response.status_code == 201:
            print(f"Successfully added hotel: {name}")
        else:
            print(f"Failed to add hotel: {name}. Status: {response.status_code}")

    print("Successfully seeded sample data via API! 🏨✨")

if __name__ == "__main__":
    seed_data()
