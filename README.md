# Hotel Reservation API

A production-ready Django REST API for managing hotels and reservations, deployed on Render with a persistent PostgreSQL database.

## 🚀 Live Base URL
`https://hotel-api-project.onrender.com/api/`

---

## 🏨 1. Get List of Hotels
Retrieve a list of all available hotels and their details (name, location, capacity).

**Endpoint:** `GET /hotels/`

**Sample Request:**
```bash
curl -X GET https://hotel-api-project.onrender.com/api/hotels/
```

**Sample Response:**
```json
[
  {
    "id": 1,
    "name": "Seaside Resort",
    "location": "Miami",
    "capacity": 200
  },
  {
    "id": 2,
    "name": "Mountain Lodge",
    "location": "Aspen",
    "capacity": 50
  }
]
```

---

## 📅 2. Post a Reservation
Create a new reservation for a specific hotel with a list of guests.

**Endpoint:** `POST /reservation/`

**Sample Request:**
```bash
curl -X POST https://hotel-api-project.onrender.com/api/reservation/ \
     -H "Content-Type: application/json" \
     -d '{
           "hotel_name": "Seaside Resort",
           "checkin": "2026-05-15",
           "checkout": "2026-05-20",
           "guests_list": [
             {"guest_name": "Alice Smith", "gender": "Female"},
             {"guest_name": "Bob Jones", "gender": "Male"}
           ]
         }'
```

**Sample Response:**
```json
{
  "hotel_name": "Seaside Resort",
  "checkin": "2026-05-15",
  "checkout": "2026-05-20",
  "guests_list": [
    {"guest_name": "Alice Smith", "gender": "Female"},
    {"guest_name": "Bob Jones", "gender": "Male"}
  ],
  "confirmation_number": "3e7d79b9-a5b5-4539-9933-dc1f0eb112da"
}
```

---

## 🛠 Features
- **Persistent Data**: Powered by a managed PostgreSQL database on Render.
- **Auto-Migrations**: Built-in `render.yaml` Blueprint ensures the database is always up to date.
- **Admin Console**: Access the backend at `/admin/` (User: `admin` / Pass: `admin123`).

## ⚙️ Deployment
This project is configured for one-click deployment via Render Blueprints using `render.yaml`.
