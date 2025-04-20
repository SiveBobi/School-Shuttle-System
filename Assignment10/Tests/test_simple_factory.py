import unittest
from creational_patterns.simple_factory import VehicleFactory

class TestSimpleFactory(unittest.TestCase):
    def test_create_car(self):
        car = VehicleFactory.create_vehicle("car")
        self.assertEqual(car.drive(), "Driving a car")

    def test_create_bike(self):
        bike = VehicleFactory.create_vehicle("bike")
        self.assertEqual(bike.drive(), "Riding a bike")

    def test_invalid_vehicle(self):
        with self.assertRaises(ValueError):
            VehicleFactory.create_vehicle("spaceship")
