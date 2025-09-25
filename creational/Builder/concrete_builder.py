from creational.Builder.builder import PizzaBuilder
from creational.Builder.product import Pizza


class MargheritaPizzaBuilder(PizzaBuilder):

    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self, dough):
        self.pizza._dough = dough  # Enum

    def set_sauce(self, sauce):
        self.pizza._sauce = sauce

    def set_topping(self, topping):
        self.pizza._topping = topping

    def get_pizza(self):
        return self.pizza


class PepperoniPizzaBuilder(PizzaBuilder):

    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self, dough):
        self.pizza._dough = dough  # Enum

    def set_sauce(self, sauce):
        self.pizza._sauce = sauce

    def set_topping(self, topping):
        self.pizza._topping = topping

    def get_pizza(self):
        return self.pizza


class VeggiePizzaBuilder(PizzaBuilder):

    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self, dough):
        self.pizza._dough = dough  # Enum

    def set_sauce(self, sauce):
        self.pizza._sauce = sauce

    def set_topping(self, topping):
        self.pizza._topping = topping

    def get_pizza(self):
        return self.pizza


class BBQChickenPizzaBuilder(PizzaBuilder):

    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self, dough):
        self.pizza._dough = dough  # Enum

    def set_sauce(self, sauce):
        self.pizza._sauce = sauce

    def set_topping(self, topping):
        self.pizza._topping = topping

    def get_pizza(self):
        return self.pizza


class HawaianaPizzaBuilder(PizzaBuilder):

    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self, dough):
        self.pizza._dough = dough  # Enum

    def set_sauce(self, sauce):
        self.pizza._sauce = sauce

    def set_topping(self, topping):
        self.pizza._topping = topping

    def get_pizza(self):
        return self.pizza
