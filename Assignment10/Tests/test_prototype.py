import unittest
from creational_patterns.prototype import ShapeCache, Circle

class TestPrototype(unittest.TestCase):
    def test_clone_circle(self):
        cache = ShapeCache()
        cache.load_shapes()
        original = cache.get_shape("circle")
        clone = cache.get_shape("circle")

        self.assertIsNot(original, clone)
        self.assertEqual(original.radius, clone.radius)
