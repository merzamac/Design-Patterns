import copy

from creational.Prototype.prototype import Prototype, Shape


class SystemConfigPrototype(Prototype):
    def __init__(self, configuration):
        self._configuration = configuration

    def clone(self):
        return copy.deepcopy(self)


class Rectangle(Shape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self._width = None
        self._height = None

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Rectangle at ({self._x}, {self._y}) with width {self._width} and height {self._height}"


class Circle(Shape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self._radius = None

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Circle at ({self._x}, {self._y}) with radius {self._radius}"
