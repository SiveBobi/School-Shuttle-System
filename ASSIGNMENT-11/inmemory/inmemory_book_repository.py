from typing import Optional, List
from repositories.book_repository import BookRepository
from src.book import Book

class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self._storage = {}

    def save(self, book: Book) -> None:
        self._storage[book.book_id] = book

    def find_by_id(self, book_id: str) -> Optional[Book]:
        return self._storage.get(book_id)

    def find_all(self) -> List[Book]:
        return list(self._storage.values())

    def delete(self, book_id: str) -> None:
        if book_id in self._storage:
            del self._storage[book_id]
