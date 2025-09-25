from creational.FactoryMethod.concrete_creator import RoadLogistics, SeaLogistics
from creational.FactoryMethod.creator import Logistics
from creational.FactoryMethod.product import Transport


def client_code(logistics: Logistics):
    transport: Transport = logistics.create_transport()
    transport.delivery()

    print(type(transport))


def factory():
    client_code(RoadLogistics())
    client_code(SeaLogistics())
