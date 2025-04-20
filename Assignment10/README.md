# 🧠 Assignment 10: From Class Diagrams to Code with Creational Patterns

## 📌 Overview

This project implements a working system in **Python**, based on the UML Class Diagram from Assignment 9, and demonstrates **all six creational design patterns**:

- ✅ Simple Factory  
- ✅ Factory Method  
- ✅ Abstract Factory  
- ✅ Builder  
- ✅ Prototype  
- ✅ Singleton  

All patterns are modularized, tested, and follow clean object-oriented principles.

---

## 📂 Project Structure

```plaintext
Assignment10/
├── src/                    # Class Implementations
├── creational_patterns/   # 6 Design Patterns
├── tests/                 # Unit Tests
├── README.md
├── CHANGELOG.md
```

Click to view content:

- 📁 [`src/`](./src) – Core system classes  
- 📁 [`creational_patterns/`](./creational_patterns) – All six creational pattern implementations  
- 📁 [`tests/`](./tests) – Unit tests for all patterns  
- 📄 [`CHANGELOG.md`](./CHANGELOG.md) – Task log and milestone tracking  

---

## ⚙️ Technologies Used

- **Language**: Python 3.10+
- **Testing Framework**: Python `unittest`
- **Optional Tools**: `coverage`, `pytest-cov`

---

## 🧩 Creational Patterns & Justification

| Pattern          | File                                                        | Purpose                                                        |
|------------------|-------------------------------------------------------------|----------------------------------------------------------------|
| Simple Factory   | [`simple_factory.py`](./creational_patterns/simple_factory.py)     | Centralized creation of `Car`, `Bike`, `Truck`                 |
| Factory Method   | [`factory_method.py`](./creational_patterns/factory_method.py)     | Subclass decision-making for `CreditCard` vs `PayPal`          |
| Abstract Factory | [`abstract_factory.py`](./creational_patterns/abstract_factory.py) | Produces compatible UI elements (buttons/checkboxes)           |
| Builder          | [`builder.py`](./creational_patterns/builder.py)                   | Builds `Pizza` step-by-step with optional ingredients           |
| Prototype        | [`prototype.py`](./creational_patterns/prototype.py)               | Clones configured shapes like `Circle`, `Rectangle`             |
| Singleton        | [`singleton.py`](./creational_patterns/singleton.py)               | Single shared `DatabaseConnection` instance                    |

---

## ✅ Class Implementations (from UML)

Classes from the class diagram are implemented in [`/src`](./src):

- [`user.py`](./src/user.py): Handles borrowing & returning  
- [`book.py`](./src/book.py): Tracks book status  
- [`loan.py`](./src/loan.py): Manages loan logic & fine calculation  
- [`fine.py`](./src/fine.py): Records fine amounts and payments  
- [`librarian.py`](./src/librarian.py): Staff issuing and accepting books  
- [`reservation.py`](./src/reservation.py): Book reservation handling  

---

## 🧪 Running Tests

All pattern tests are in [`/tests`](./tests). To run all tests:

```bash
python -m unittest discover tests
```

To run with **coverage** (optional):

```bash
pip install coverage
coverage run -m unittest discover tests
coverage report
```

All patterns are tested for:
- Correct object creation  
- Attribute correctness  
- Singleton instance validation  
- Prototype clone independence  
- Builder step-by-step integrity

---

## 📊 Project Tracking

- Tasks & implementation milestones are tracked in [`CHANGELOG.md`](./CHANGELOG.md)
- Issues/bugs managed via GitHub Projects
- Code is modular, testable, and scalable

---

## 👤 Author

**Sive Bobi**  
📚 Course: Software Engineering  
🧾 Assignment 10 – Software Design & Creational Patterns  
📅 April 2025

---
