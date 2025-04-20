class Book:
    def __init__(self, book_id, title, author, isbn, status='Available'):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def check_out(self):
        self.status = 'CheckedOut'

    def return_book(self):
        self.status = 'Available'
