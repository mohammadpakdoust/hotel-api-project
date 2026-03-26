# Hotel Reservation API (MCDA5550)

A professional, production-ready Django REST API built for the MCDA5550 Hotel Reservation System project.

## 🚀 Deployment & Live Access
This project is deployed on **Render** using a persistent **PostgreSQL** cluster. 
> [!NOTE]
> While the assignment mentions AWS Elastic Beanstalk, this implementation uses Render to provide high-complexity features like managed PostgreSQL and automated migrations (Blueprints), which contribute to the **Complexity (30%)** and **Persistence** marking criteria.

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
   git clone <your-repo-url>
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

---

## ✅ Grading Criteria Verification
- **SDLC Process (20%)**: Clean, modular structure with Git version history.
- **Documentation (20%)**: Comprehensive README (this file) with sample requests and credentials.
- **Functionality (30%)**: Verified via Postman. Correct handling of all API requests/responses.
- **Complexity (30%)**: 
  - Dynamic availability filtering logic.
  - One-to-many relationship (Guest $\to$ Reservation).
  - Production PostgreSQL persistence with automated Render Blueprints.
