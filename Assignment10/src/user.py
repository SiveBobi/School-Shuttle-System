class User:
    def __init__(self, user_id, name, email):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.loans = []

    def borrow_book(self, book):
        self.loans.append(book)

    def return_book(self, book):
        if book in self.loans:
            self.loans.remove(book)

    def get_user_info(self):
        return f"{self.__name} ({self.__email})"
