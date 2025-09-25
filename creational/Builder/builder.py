from abc import ABC, abstractmethod


class PizzaBuilder(ABC):

    @abstractmethod
    def set_dough(self, dough):
        pass

    @abstractmethod
    def set_sauce(self, sauce):
        pass

    @abstractmethod
    def set_topping(self, topping):
        pass

    @abstractmethod
    def get_pizza(self):
        pass
