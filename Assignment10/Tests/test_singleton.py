import unittest
from creational_patterns.singleton import DatabaseConnection

class TestSingleton(unittest.TestCase):
    def test_single_instance(self):
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()
        self.assertIs(db1, db2)

    def test_connection_string(self):
        db = DatabaseConnection()
        self.assertEqual(db.get_connection(), "Connected to DB")
