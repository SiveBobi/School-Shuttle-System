from repositories.book_repository import BookRepository
from src.book import Book

class BookService:
    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    def create_book(self, book: Book) -> None:
        self.book_repo.save(book)

    def get_all_books(self):
        return self.book_repo.find_all()

    def update_book(self, book_id: str, updated_book: Book) -> None:
        existing = self.book_repo.find_by_id(book_id)
        if not existing:
            raise ValueError("Book not found")
        self.book_repo.save(updated_book)

    def checkout_book(self, book_id: str) -> Book:
        book = self.book_repo.find_by_id(book_id)
        if not book:
            raise ValueError("Book not found")
        if book.status == "checked_out":
            raise ValueError("Book already checked out")
        book.status = "checked_out"
        self.book_repo.save(book)
        return book
