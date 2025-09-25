from creational.FactoryMethod.concrete_product import Ship, Truck
from creational.FactoryMethod.creator import Logistics


class RoadLogistics(Logistics):
    def create_transport(self) -> Truck:
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self) -> Ship:
        return Ship()
