from creational.AbstractFactory.concrete_product import (
    ArtDecoChair,
    ArtDecoCoffeeTable,
    ArtDecoSofa,
    ModernChair,
    ModernCoffeeTable,
    ModernSofa,
    VictorianChair,
    VictorianCoffeeTable,
    VictorianSofa,
)
from creational.AbstractFactory.product import FurnitureFactory


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> VictorianChair:
        return VictorianChair()

    def create_coffee_table(self) -> VictorianCoffeeTable:
        return VictorianCoffeeTable()

    def create_sofa(self) -> VictorianSofa:
        return VictorianSofa()


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> ModernChair:
        return ModernChair()

    def create_coffee_table(self) -> ModernCoffeeTable:
        return ModernCoffeeTable()

    def create_sofa(self) -> ModernSofa:
        return ModernSofa()


class ArtDecoFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> ArtDecoChair:
        return ArtDecoChair()

    def create_coffee_table(self) -> ArtDecoCoffeeTable:
        return ArtDecoCoffeeTable()

    def create_sofa(self) -> ArtDecoSofa:
        return ArtDecoSofa()
