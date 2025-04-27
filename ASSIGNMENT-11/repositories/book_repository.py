from .repository import Repository
from src.book import Book

class BookRepository(Repository[Book, str]):
    """Book Repository extends the generic Repository for Book objects."""
    pass
