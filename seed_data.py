import os
import django
import random
from datetime import date, timedelta

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotel_api.settings")
django.setup()

from reservations.models import Hotel, Reservation, Guest

def seed_data():
    hotel_names = [
        "Grand Plaza Hotel", "Ocean View Resort", "Mountain Retreat", 
        "Urban Oasis", "The Ritz Carlton", "Hilton Garden Inn", 
        "Marriott Riverside", "Sunset Boutique Hotel", "Crystal Palace", 
        "Emerald Suites", "Sapphire Sands", "The Continental", 
        "Metropolitan Inn", "Regency Park", "Heritage Lodge"
    ]

    guest_names = [
        "Alice Johnson", "Bob Smith", "Charlie Brown", "Diana Prince", 
        "Edward Norton", "Fiona Gallagher", "George Miller", "Hannah Montana", 
        "Ian Wright", "Jane Doe", "Kevin Spacey", "Laura Palmer"
    ]

    genders = ["Male", "Female", "Non-binary", "Other"]

    print("Cleaning old data...")
    Guest.objects.all().delete()
    Reservation.objects.all().delete()
    Hotel.objects.all().delete()

    print(f"Creating {len(hotel_names)} hotels...")
    for name in hotel_names:
        hotel = Hotel.objects.create(name=name)
        
        # Create 1-3 random reservations for each hotel
        for _ in range(random.randint(1, 3)):
            checkin = date.today() + timedelta(days=random.randint(1, 30))
            checkout = checkin + timedelta(days=random.randint(1, 7))
            
            res = Reservation.objects.create(
                hotel=hotel,
                checkin=checkin,
                checkout=checkout
            )
            
            # Create 1-2 guests for each reservation
            for _ in range(random.randint(1, 2)):
                Guest.objects.create(
                    reservation=res,
                    guest_name=random.choice(guest_names),
                    gender=random.choice(genders)
                )

    print("Successfully seeded sample data! 🏨✨")

if __name__ == "__main__":
    seed_data()
