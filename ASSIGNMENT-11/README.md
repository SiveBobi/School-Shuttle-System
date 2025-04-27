# 📚 Persistence Repository Layer – Assignment 11

---

## 📂 Folder Structure

```plaintext
/repositories/
    repository.py                # Generic Repository Interface
    book_repository.py            # Book-specific Repository Interface
    user_repository.py            # User-specific Repository Interface
    loan_repository.py            # Loan-specific Repository Interface
    reservation_repository.py     # Reservation-specific Repository Interface

/repositories/inmemory/
    inmemory_book_repository.py   # In-Memory Book Repository
    inmemory_user_repository.py   # In-Memory User Repository
    inmemory_loan_repository.py   # In-Memory Loan Repository
    inmemory_reservation_repository.py # In-Memory Reservation Repository

/repositories/filesystem/
    filesystem_book_repository.py # (Stub) JSON-based Book Repository

/factories/
    repository_factory.py         # Factory to select storage backend
/tests/
    test_inmemory_book_repository.py # Unit test for In-Memory Book Repository
```

---

## 🧩 About the Repository Layer

✅ **Repository Pattern**  
- Provides a clean abstraction over the storage mechanism (Memory, File, Database).
- All business logic talks to repository interfaces, NOT to storage directly.

✅ **Generic + Entity-Specific Interfaces**  
- Used `TypeVar` and `Generic` to create flexible, reusable repository base classes.

✅ **In-Memory Implementations**  
- Implemented using Python dictionaries (HashMaps).
- Fast, simple for development and unit testing.

✅ **Factory Pattern**  
- `RepositoryFactory` dynamically provides repository instances based on storage type (`MEMORY`, `FILESYSTEM`, `DATABASE`).
- Easy to switch storage backend without changing business logic.

✅ **Future-Proofing**  
- Added a `FileSystemBookRepository` stub for saving to JSON files.
- Designed to add databases (SQL, NoSQL) easily later.

✅ **Unit Testing**  
- `/tests/` folder contains tests verifying CRUD operations for in-memory repositories.
- Test Coverage: Create, Read, Update, Delete working for Book objects.

---

## ⚡ How to Run Unit Tests

```bash
python -m unittest discover tests
```

✅ Make sure your `/src/` and `/repositories/` are correctly structured.  
✅ No database required — runs fully in memory!

---

## 🧠 Why This Matters

- 🧼 Clean separation of concerns
- 🏗️ Scalable design
- 🔥 Easily extendable (FileSystem, SQL, MongoDB, REST APIs)
- 🎯 Ready for real-world projects

---

# 👤 Author

**Sive Bobi**  
Software Engineering  
Assignment 11 – Persistence Layer Design

---
