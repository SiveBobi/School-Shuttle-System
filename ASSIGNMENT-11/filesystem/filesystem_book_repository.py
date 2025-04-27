import json
import os
from typing import Optional, List
from repositories.book_repository import BookRepository
from src.book import Book

class FileSystemBookRepository(BookRepository):
    def __init__(self, file_path: str = "books.json"):
        self.file_path = file_path
        # Initialize empty JSON file if it doesn't exist
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                json.dump({}, f)

    def save(self, book: Book) -> None:
        books = self._load_all()
        books[book.book_id] = vars(book)
        with open(self.file_path, 'w') as f:
            json.dump(books, f)

    def find_by_id(self, book_id: str) -> Optional[Book]:
        books = self._load_all()
        book_data = books.get(book_id)
        if book_data:
            return Book(**book_data)
        return None

    def find_all(self) -> List[Book]:
        books = self._load_all()
        return [Book(**data) for data in books.values()]

    def delete(self, book_id: str) -> None:
        books = self._load_all()
        if book_id in books:
            del books[book_id]
            with open(self.file_path, 'w') as f:
                json.dump(books, f)

    def _load_all(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)
