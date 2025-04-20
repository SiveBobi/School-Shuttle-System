class Pizza:
    def __init__(self):
        self.ingredients = []

    def __str__(self):
        return f"Pizza with: {', '.join(self.ingredients)}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_cheese(self):
        self.pizza.ingredients.append("Cheese")
        return self

    def add_pepperoni(self):
        self.pizza.ingredients.append("Pepperoni")
        return self

    def add_olives(self):
        self.pizza.ingredients.append("Olives")
        return self

    def build(self):
        return self.pizza
