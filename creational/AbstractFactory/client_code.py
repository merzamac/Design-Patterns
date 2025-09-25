from creational.AbstractFactory.concrete_factory import (
    ArtDecoFurnitureFactory,
    ModernFurnitureFactory,
    VictorianFurnitureFactory,
)
from creational.AbstractFactory.product import (
    Chair,
    CoffeeTable,
    FurnitureFactory,
    Sofa,
)


def client_code(factory: FurnitureFactory):
    chair: Chair = factory.create_chair()
    coffee_table: CoffeeTable = factory.create_coffee_table()
    sofa: Sofa = factory.create_sofa()

    chair.sit_on()
    sofa.sit_on()
    coffee_table.sit_on()

    print("\n----------------------------------")


def abstract():
    client_code(ArtDecoFurnitureFactory())
    client_code(ModernFurnitureFactory())
    client_code(VictorianFurnitureFactory())
