from repositories.loan_repository import LoanRepository
from repositories.book_repository import BookRepository
from repositories.user_repository import UserRepository
from src.loan import Loan
from datetime import datetime

class LoanService:
    def __init__(self, loan_repo: LoanRepository, book_repo: BookRepository, user_repo: UserRepository):
        self.loan_repo = loan_repo
        self.book_repo = book_repo
        self.user_repo = user_repo

    def create_loan(self, loan: Loan) -> None:
        # Check book exists
        book = self.book_repo.find_by_id(loan.book_id)
        if not book:
            raise ValueError("Book not found")

        # Check user exists
        user = self.user_repo.find_by_id(loan.user_id)
        if not user:
            raise ValueError("User not found")

        # Limit user to max 5 books
        user_loans = [l for l in self.loan_repo.find_all() if l.user_id == loan.user_id]
        if len(user_loans) >= 5:
            raise ValueError("User has reached the loan limit (5 books)")

        loan.date_borrowed = str(datetime.now())
        self.loan_repo.save(loan)
