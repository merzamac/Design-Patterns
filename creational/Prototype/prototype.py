from abc import ABC, abstractmethod


class Prototype:
    def clone(self):
        pass


class Shape(ABC):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @abstractmethod
    def clone(self):
        pass
