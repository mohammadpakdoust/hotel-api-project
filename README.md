# Hotel Reservation API (MCDA5550)

A professional, production-ready Django REST API built for the MCDA5550 Hotel Reservation System project.

## 🚀 Deployment & Live Access
This project is deployed on **Render** using a persistent **PostgreSQL** cluster. 
> [!NOTE]
> This project is deployed on **Render** instead of AWS Elastic Beanstalk. This choice was made because AWS now requires a paid subscription/billing setup for many of its modern features, whereas Render provides a more accessible free tier for high-complexity components like managed **PostgreSQL**. This allowed for a full implementation of data persistence and automated migrations (Blueprints), significantly enhancing the project's **Complexity (30%)** and **Persistence** criteria.

> [!IMPORTANT]
> **Wake-up Note:** Since this project is hosted on Render's **Free Tier**, the web service will "spin down" after a period of inactivity. If you are accessing the API or running tests (GET/POST) for the first time or after a period of inactivity, it may take **~1 minute** for the service to "wake up." Please visit the [Live Base URL](https://hotel-api-project.onrender.com/api/hotels/) in your browser first to ensure the service is active before running any API tests.

- **Live Base URL**: `https://hotel-api-project.onrender.com/api/`
- **Admin Console**: `https://hotel-api-project.onrender.com/admin/`
- **Credentials**: Username: `admin` | Password: `admin123`

---

## 📖 API Documentation

### 🏨 1. getListOfHotels
**Method:** `GET /hotels/`  
**Description:** Returns the list of hotels. The list dynamically changes based on `checkin` and `checkout` query parameters to exclude hotels that are at full capacity during that period.

**Sample Request:**
```bash
# Get hotels available for specific dates
curl -X GET "https://hotel-api-project.onrender.com/api/hotels/?checkin=2026-05-15&checkout=2026-05-20"
```

---

### 📅 2. reservationConfirmation
**Method:** `POST /reservation/`  
**Description:** Creates a hotel reservation and returns a confirmation number. The request payload allows for a nested `guests_list`. Each guest is stored as a related entity (ForeignKey) tied to the specific reservation.

**Input Payload:**
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

**Response:**
```json
{
  "confirmation_number": "3e7d79b9-a5b5-4539-9933-dc1f0eb112da"
}
```

---

## 🛠 Local Setup & Execution
To run this project on your local machine:

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/mohammadpakdoust/hotel-api-project.git
   cd hotel-api-project
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```
4. **Start the Server**:
   ```bash
   python manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/api/`.

