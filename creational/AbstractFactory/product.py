from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def has_legs(self):
        pass

    @abstractmethod
    def sit_on(self):
        pass


class CoffeeTable(ABC):
    @abstractmethod
    def has_legs(self):
        pass

    @abstractmethod
    def sit_on(self):
        pass


class Sofa(ABC):
    @abstractmethod
    def has_legs(self):
        pass

    @abstractmethod
    def sit_on(self):
        pass


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_coffee_table(self) -> CoffeeTable:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass
