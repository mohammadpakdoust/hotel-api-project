# Hotel Reservation API

A production-ready Django REST API for managing hotels and reservations, specifically aligned with assignment requirements.

## 🚀 Live Base URL
`https://hotel-api-project.onrender.com/api/`

---

## 🏨 1. Get List of Hotels (Available Hotels)
Retrieve a list of hotels. The list dynamically filters based on availability if `checkin` and `checkout` dates are provided.

**Endpoint:** `GET /hotels/`

**Query Parameters (Optional):**
- `checkin`: (e.g., `2026-05-15`)
- `checkout`: (e.g., `2026-05-20`)

**Sample Request:**
```bash
# Get all hotels
curl -X GET https://hotel-api-project.onrender.com/api/hotels/

# Get hotels available for specific dates
curl -X GET "https://hotel-api-project.onrender.com/api/hotels/?checkin=2026-05-15&checkout=2026-05-20"
```

**Sample Response:**
```json
[
  {
    "id": 1,
    "name": "Seaside Resort",
    "location": "Miami",
    "capacity": 200
  }
]
```

---

## 📅 2. Post a Reservation (reservationConfirmation)
Create a new reservation. This endpoint returns only the confirmation number. All guests are automatically associated with the reservation record in the database.

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
  "confirmation_number": "3e7d79b9-a5b5-4539-9933-dc1f0eb112da"
}
```

---

## 🛠 Features
- **Strict Data Relationships**: Each guest record references its specific reservation via a Foreign Key.
- **Availability Logic**: Hotels are automatically excluded from the list if their capacity is reached during the requested period.
- **Persistent Data**: Powered by a managed PostgreSQL database on Render.
- **Admin Console**: Access the backend at `/admin/` (User: `admin` / Pass: `admin123`).
