```mermaid
classDiagram
    class User {
        - userId: String
        - name: String
        - email: String
        + borrowBook(): void
        + returnBook(): void
    }
    class Book {
        - bookId: String
        - title: String
        - author: String
        - ISBN: String
        - status: String
        + checkOut(): void
        + return(): void
    }
    class Loan {
        - loanId: String
        - dueDate: Date
        - status: String
        + calculateFine(): float
        + closeLoan(): void
    }
    class Librarian {
        - staffId: String
        - name: String
        - email: String
        + issueBook(): void
        + acceptReturn(): void
    }
    class Reservation {
        - reservationId: String
        - dateReserved: Date
        + cancelReservation(): void
    }
    class Fine {
        - fineId: String
        - amount: float
        - isPaid: Boolean
        + payFine(): void
    }
    User "1" --> "0..*" Loan : borrows
    Loan "1" --> "1" Book : for
    Loan "1" --> "1" User : issuedTo
    Loan "1" --> "0..1" Fine : mayHave
    Librarian "1" --> "0..*" Loan : manages
    Reservation "1" --> "1" User : madeBy
    Reservation "1" --> "1" Book : reserves


