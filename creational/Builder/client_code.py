from creational.Builder.builder import PizzaBuilder
from creational.Builder.concrete_builder import (
    BBQChickenPizzaBuilder,
    HawaianaPizzaBuilder,
    MargheritaPizzaBuilder,
    PepperoniPizzaBuilder,
    VeggiePizzaBuilder,
)
from creational.Builder.director import Cook


def client_code(builder: PizzaBuilder):
    cook = Cook()
    pizza = cook.make_pizza(builder)
    print(pizza, type(builder))


def builder():
    client_code(MargheritaPizzaBuilder())
    client_code(PepperoniPizzaBuilder())
    client_code(VeggiePizzaBuilder())
    client_code(HawaianaPizzaBuilder())
    client_code(BBQChickenPizzaBuilder())
