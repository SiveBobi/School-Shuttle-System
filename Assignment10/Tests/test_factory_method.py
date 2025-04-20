import unittest
from creational_patterns.factory_method import CreditCardFactory, PayPalFactory

class TestFactoryMethod(unittest.TestCase):
    def test_credit_card_payment(self):
        factory = CreditCardFactory()
        processor = factory.create_processor()
        result = processor.process_payment(100)
        self.assertIn("credit card", result)

    def test_paypal_payment(self):
        factory = PayPalFactory()
        processor = factory.create_processor()
        result = processor.process_payment(50)
        self.assertIn("PayPal", result)
