# 📦 CHANGELOG.md – Assignment 10: From Class Diagrams to Code

## Version 1.0.0 – [Initial Release] – 2025-04-21

### ✅ Deliverable 1: Class Implementation (`/src`)
- Implemented core domain classes from the class diagram:
  - `User`, `Book`, `Loan`, `Fine`, `Librarian`, `Reservation`
- Encapsulated fields with basic logic (e.g., check_out, return, borrow_book)
- Established composition between User → Loan, Book → Loan

### ✅ Deliverable 2: Creational Pattern Implementation (`/creational_patterns`)
- Implemented **6 Creational Design Patterns**:
  - `Simple Factory` → `VehicleFactory` (Car, Bike, Truck)
  - `Factory Method` → `PaymentFactory` (CreditCard, PayPal)
  - `Abstract Factory` → `GUIFactory` (Windows/Mac Button & Checkbox)
  - `Builder` → `PizzaBuilder`
  - `Prototype` → `ShapeCache` with cloning
  - `Singleton` → `DatabaseConnection` (Thread-safe)

### ✅ Deliverable 3: Unit Testing (`/tests`)
- Created test files for each design pattern
- Verified correct instantiation, behavior, and edge cases:
  - Singleton is enforced
  - Prototype clones are deep copies
  - Builder assembles complex objects correctly
- All tests pass successfully using Python's `unittest` module

### ⚙️ Tools & Environment
- Language: **Python 3.10+**
- Testing: `unittest`, `coverage` (optional)
- Folder structure adheres to GitHub assignment specification

---

## Upcoming (v1.1.0)
- Add README usage examples for each pattern
- Optional: Refactor with interfaces using `abc.ABC` for consistency

---

