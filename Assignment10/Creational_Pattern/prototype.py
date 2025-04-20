import copy

class Shape:
    def clone(self):
        return copy.deepcopy(self)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle with radius {self.radius}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle {self.width}x{self.height}"

class ShapeCache:
    def __init__(self):
        self.cache = {}

    def load_shapes(self):
        self.cache["circle"] = Circle(5)
        self.cache["rectangle"] = Rectangle(4, 6)

    def get_shape(self, shape_type):
        shape = self.cache.get(shape_type)
        return shape.clone() if shape else None
