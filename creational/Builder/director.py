from functools import singledispatchmethod

from creational.Builder.builder import PizzaBuilder
from creational.Builder.concrete_builder import (
    BBQChickenPizzaBuilder,
    HawaianaPizzaBuilder,
    MargheritaPizzaBuilder,
    PepperoniPizzaBuilder,
    VeggiePizzaBuilder,
)
from creational.Builder.types import Dough, Sauce, Topping


class Cook:
    """Director"""

    @singledispatchmethod
    def make_pizza(self, builder):
        raise NotImplementedError("Tipo no soportado")

    @make_pizza.register
    def _(self, builder: MargheritaPizzaBuilder):
        """Pizza Margherita clásica"""
        builder.set_dough(Dough.THIN.value)
        builder.set_sauce(Sauce.TOMATO.value)
        builder.set_topping([Topping.MOZZARELLA.value, Topping.BASIL.value])
        return builder.get_pizza()

    @make_pizza.register
    def _(self, builder: PepperoniPizzaBuilder):
        """Pizza Pepperoni popular"""
        builder.set_dough(Dough.TRADITIONAL.value)
        builder.set_sauce(Sauce.TOMATO.value)
        builder.set_topping([Topping.MOZZARELLA.value, Topping.PEPPERONI.value])
        return builder.get_pizza()

    @make_pizza.register
    def _(self, builder: VeggiePizzaBuilder):
        """Pizza vegetariana"""
        builder.set_dough(Dough.THIN.value)
        builder.set_sauce(Sauce.TOMATO.value)
        builder.set_topping(
            [
                Topping.MOZZARELLA.value,
                Topping.BELL_PEPPERS.value,
                Topping.MUSHROOMS.value,
                Topping.ONIONS.value,
            ]
        )
        return builder.get_pizza()

    @make_pizza.register
    def _(self, builder: BBQChickenPizzaBuilder):
        """Pizza con pollo BBQ"""
        builder.set_dough(Dough.TRADITIONAL.value)
        builder.set_sauce(Sauce.BBQ.value)
        builder.set_topping(
            [
                Topping.MOZZARELLA.value,
                Topping.CHICKEN.value,
                Topping.RED_ONIONS.value,
                Topping.CILANTRO.value,
            ]
        )
        return builder.get_pizza()

    @make_pizza.register
    def _(self, builder: HawaianaPizzaBuilder):
        """Pizza Hawaiana (controversial pero popular)"""
        builder.set_dough(Dough.TRADITIONAL.value)
        builder.set_sauce(Sauce.TOMATO.value)
        builder.set_topping(
            [Topping.MOZZARELLA.value, Topping.HAM.value, Topping.PINEAPPLE.value]
        )
        return builder.get_pizza()
