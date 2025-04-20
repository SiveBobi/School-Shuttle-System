from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"

class PaymentFactory(ABC):
    @abstractmethod
    def create_processor(self) -> PaymentProcessor:
        pass

class CreditCardFactory(PaymentFactory):
    def create_processor(self):
        return CreditCardProcessor()

class PayPalFactory(PaymentFactory):
    def create_processor(self):
        return PayPalProcessor()
