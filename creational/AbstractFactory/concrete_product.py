from creational.AbstractFactory.product import Chair, CoffeeTable, Sofa


class VictorianChair(Chair):
    def sit_on(self):
        print("Victorian Chair")

    def has_legs(self):
        return True


class ModernChair(Chair):
    def sit_on(self):
        print("Modern Chair")

    def has_legs(self):
        return True


class ArtDecoChair(Chair):
    def sit_on(self):
        print("Art Deco Chair")

    def has_legs(self):
        return True


class ModernSofa(Sofa):
    def sit_on(self):
        print("Modern Sofa")

    def has_legs(self):
        return True


class ArtDecoSofa(Sofa):
    def sit_on(self):
        print("Art Deco Sofa")

    def has_legs(self):
        return True


class VictorianSofa(Sofa):
    def sit_on(self):
        print("Victorian Sofa")

    def has_legs(self):
        return True


class VictorianCoffeeTable(CoffeeTable):
    def sit_on(self):
        print("Victorian Coffee Table")

    def has_legs(self):
        return True


class ModernCoffeeTable(CoffeeTable):
    def sit_on(self):
        print("Modern Coffee Table")

    def has_legs(self):
        return True


class ArtDecoCoffeeTable(CoffeeTable):
    def sit_on(self):
        print("Art Deco Coffee Table")

    def has_legs(self):
        return True
