from creational.FactoryMethod.product import Transport


class Ship(Transport):
    def delivery(self):
        print("Entregado por mar en un contenerdor.")


class Truck(Transport):

    def delivery(self):
        print(f"Entregado por tierra en una caja")
