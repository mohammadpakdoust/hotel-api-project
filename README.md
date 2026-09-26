# Hotel Reservation REST API

A Django REST API for hotel availability and reservation workflows, with PostgreSQL persistence and a live deployment on Render.

## Live deployment

- **Base API:** https://hotel-api-project.onrender.com/api/
- **Hotels endpoint:** https://hotel-api-project.onrender.com/api/hotels/

> The service may take a short time to wake after inactivity when running on a free hosting tier.

## API

### List available hotels

```http
GET /api/hotels/?checkin=2026-05-15&checkout=2026-05-20
```

The endpoint returns hotels with availability for the requested date range.

### Create a reservation

```http
POST /api/reservation/
Content-Type: application/json
```

Example payload:

```json
{
  "hotel_name": "Seaside Resort",
  "checkin": "2026-05-15",
  "checkout": "2026-05-20",
  "guests_list": [
    {"guest_name": "Alice Smith", "gender": "Female"},
    {"guest_name": "Bob Jones", "gender": "Male"}
  ]
}
```

Example response:

```json
{
  "confirmation_number": "3e7d79b9-a5b5-4539-9933-dc1f0eb112da"
}
```

## Tech stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Render

## Run locally

```bash
git clone https://github.com/mohammadpakdoust/hotel-api-project.git
cd hotel-api-project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/api/
```

## Security note

Administrative credentials are intentionally **not** published in this repository. Configure privileged access through environment-specific secrets and deployment settings.

## Background

Originally developed for MCDA coursework at Saint Mary's University and presented here as a backend/API portfolio project.
