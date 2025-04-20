from datetime import date

class Loan:
    def __init__(self, loan_id, user, book, due_date: date, status='Active'):
        self.loan_id = loan_id
        self.user = user
        self.book = book
        self.due_date = due_date
        self.status = status

    def close_loan(self):
        self.status = 'Closed'

    def calculate_fine(self, current_date: date):
        if current_date > self.due_date:
            return (current_date - self.due_date).days * 2  # 2 currency units per day
        return 0
