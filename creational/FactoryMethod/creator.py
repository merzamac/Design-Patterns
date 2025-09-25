from abc import ABC, abstractmethod

from creational.FactoryMethod.product import Transport


class Logistics:
    @abstractmethod
    def create_transport(self) -> Transport:
        pass
