# 📚 Library Management System – REST API

This project is part of a series of assignments for the Software Engineering course by **Sive Bobi**. It demonstrates a fully layered architecture using best practices such as Repository Pattern, Service Layer, Factory Pattern, and REST API exposure with FastAPI.

---

## 🔧 Technologies Used

- ✅ **Python 3.10+**
- ✅ **FastAPI** for REST APIs
- ✅ **Pydantic** for schema validation
- ✅ **Swagger / OpenAPI** (auto-generated docs)
- ✅ **Unit + Integration Testing** with `unittest` & `TestClient`
- ✅ **Repository Pattern** (In-Memory + Factory support)

---

## 🧱 Architecture Overview

```plaintext
src/
├── book.py           # Book model
├── user.py           # User model
├── loan.py           # Loan model

repositories/
├── repository.py
├── book_repository.py
├── /inmemory/
│   ├── inmemory_book_repository.py
│   └── ...
├── /filesystem/
│   └── filesystem_book_repository.py (stub)

services/
├── book_service.py
├── user_service.py
└── loan_service.py

api/
├── book_api.py
├── user_api.py
└── loan_api.py

docs/
├── swagger-ui.png
├── swagger.md
└── openapi.json (optional)

tests/
├── services/
│   └── test_loan_service.py
└── api/
    └── test_books.py

main.py
