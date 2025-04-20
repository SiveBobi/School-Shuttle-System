import unittest
from creational_patterns.builder import PizzaBuilder

class TestBuilder(unittest.TestCase):
    def test_pizza_with_toppings(self):
        builder = PizzaBuilder()
        pizza = builder.add_cheese().add_pepperoni().add_olives().build()
        self.assertIn("Cheese", str(pizza))
        self.assertIn("Pepperoni", str(pizza))
        self.assertIn("Olives", str(pizza))

    def test_empty_pizza(self):
        pizza = PizzaBuilder().build()
        self.assertEqual(str(pizza), "Pizza with: ")
