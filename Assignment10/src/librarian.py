class Librarian:
    def __init__(self, staff_id, name, email):
        self.staff_id = staff_id
        self.name = name
        self.email = email

    def issue_book(self, user, book):
        if book.status == "Available":
            user.borrow_book(book)
            book.check_out()
        else:
            print("Book is not available for checkout.")

    def accept_return(self, user, book):
        user.return_book(book)
        book.return_book()
