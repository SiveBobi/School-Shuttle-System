from fastapi import APIRouter, HTTPException
from services.book_service import BookService
from repositories.inmemory.inmemory_book_repository import InMemoryBookRepository
from src.book import Book

router = APIRouter(prefix="/api/books", tags=["Books"])

book_service = BookService(InMemoryBookRepository())

@router.get("/")
def get_all_books():
    return book_service.get_all_books()

@router.post("/")
def create_book(book: Book):
    book_service.create_book(book)
    return {"message": "Book created successfully"}

@router.put("/{book_id}")
def update_book(book_id: str, updated_book: Book):
    try:
        book_service.update_book(book_id, updated_book)
        return {"message": "Book updated"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/{book_id}/checkout")
def checkout_book(book_id: str):
    try:
        book = book_service.checkout_book(book_id)
        return {"message": f"Book {book_id} checked out", "book": book}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
