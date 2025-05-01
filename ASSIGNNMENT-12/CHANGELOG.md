# 📦 CHANGELOG

## 📌 Assignment 12: Service Layer and REST API

---

### ✅ [NEW] Service Layer

- Created `/services/book_service.py` for book business logic
- Created `/services/user_service.py` for user management
- Created `/services/loan_service.py` with loan limit rules (max 5 books)
- Added unit tests in `/tests/services/test_loan_service.py`

---

### ✅ [NEW] REST API (FastAPI)

- Created `/api/book_api.py` with endpoints:
  - `GET /api/books`
  - `POST /api/books`
  - `PUT /api/books/{id}`
  - `POST /api/books/{id}/checkout`
- Created `/api/user_api.py` with:
  - `GET /api/users`
  - `POST /api/users`
  - `GET /api/users/{id}`
- Created `/api/loan_api.py`:
  - `POST /api/loans`

- Connected all APIs through `main.py`

---

### ✅ [NEW] API Documentation

- Auto-generated Swagger UI via FastAPI
- Added `/docs/swagger-ui.png` screenshot
- Wrote `/docs/swagger.md` to explain documentation setup
- (Optional) Included exported OpenAPI spec `/docs/openapi.json`

---

### 🐛 Bugs & Fixes

- Fixed `ValueError` handling with HTTP 400/404 using FastAPI `HTTPException`
- Ensured repositories are injected using in-memory factory

---

### 📌 GitHub Project Tracking

- Closed issues for:  
  `BookService`, `Loan limit validation`, `FastAPI book routes`, `Swagger setup`
- Linked commits using:  
  `git commit -m "Close #12: Implement book checkout API"`

---

### 🛠 Tech Stack

- **FastAPI** for REST API  
- **Python** services and models  
- **In-memory repos** from Assignment 11  
- **Swagger/OpenAPI** auto-generated

---

### ✍️ Author

**Sive Bobi**  
Software Engineering — Backend REST API

---
