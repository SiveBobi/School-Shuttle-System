class Fine:
    def __init__(self, fine_id, amount=0.0):
        self.fine_id = fine_id
        self.amount = amount
        self.is_paid = False

    def pay_fine(self):
        self.is_paid = True
