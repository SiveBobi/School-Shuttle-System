class Reservation:
    def __init__(self, reservation_id, user, book, date_reserved):
        self.reservation_id = reservation_id
        self.user = user
        self.book = book
        self.date_reserved = date_reserved

    def cancel_reservation(self):
        self.book.status = 'Available'
