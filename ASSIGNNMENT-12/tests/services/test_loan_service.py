import unittest
from services.loan_service import LoanService
from repositories.inmemory.inmemory_loan_repository import InMemoryLoanRepository
from repositories.inmemory.inmemory_book_repository import InMemoryBookRepository
from repositories.inmemory.inmemory_user_repository import InMemoryUserRepository
from src.book import Book
from src.user import User
from src.loan import Loan

class TestLoanService(unittest.TestCase):
    def setUp(self):
        self.book_repo = InMemoryBookRepository()
        self.user_repo = InMemoryUserRepository()
        self.loan_repo = InMemoryLoanRepository()
        self.service = LoanService(self.loan_repo, self.book_repo, self.user_repo)

        self.book = Book(book_id="B1", title="Python 101", author="Sive", isbn="123", status="available")
        self.user = User(user_id="U1", name="Bob", email="bob@example.com")

        self.book_repo.save(self.book)
        self.user_repo.save(self.user)

    def test_create_loan_success(self):
        loan = Loan(loan_id="L1", book_id="B1", user_id="U1", date_borrowed="", due_date="")
        self.service.create_loan(loan)
        self.assertEqual(len(self.loan_repo.find_all()), 1)

    def test_loan_limit_exceeded(self):
        for i in range(5):
            loan = Loan(loan_id=f"L{i}", book_id="B1", user_id="U1", date_borrowed="", due_date="")
            self.loan_repo.save(loan)

        with self.assertRaises(ValueError):
            self.service.create_loan(Loan(loan_id="L6", book_id="B1", user_id="U1", date_borrowed="", due_date=""))
