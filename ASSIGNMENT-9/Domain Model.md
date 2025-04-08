# 📘 Domain Modeling and Class Diagram Development

## 🎯 Objective

1. Develop a detailed Domain Model to represent key entities, relationships, and business logic.
2. Create a Class Diagram using Mermaid.js to visualize system structure.
3. Reflect on challenges and insights from the design process.

---

## 🔷 1. Domain Model (30 Marks)

| Entity     | Attributes                                 | Methods                          | Relationships                              |
|------------|--------------------------------------------|----------------------------------|--------------------------------------------|
| User       | userId, name, email                        | borrowBook(), returnBook()       | Borrows Loan(s)                            |
| Book       | bookId, title, author, ISBN, status        | checkOut(), return()             | Associated with Loan                       |
| Loan       | loanId, dueDate, status                    | calculateFine(), closeLoan()     | Links User and Book                        |
| Librarian  | staffId, name, email                       | issueBook(), acceptReturn()      | Manages Loans                              |
| Reservation| reservationId, dateReserved                | cancelReservation()              | Linked to Book and User                    |
| Fine       | fineId, amount, isPaid                     | payFine()                        | Related to Loan                            |

### 🧾 Business Rules

- A user can borrow a **maximum of 5 books**.
- A book can only be borrowed if its status is **"Available"**.
- A loan becomes **overdue** if the due date is passed and the book isn’t returned.
- Only a librarian can issue or accept returned books.
- Fines must be paid before new loans can be issued.

---


 
