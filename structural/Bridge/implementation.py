from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def is_enabled(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass

    @abstractmethod
    def set_volume(self, percent):
        pass

    @abstractmethod
    def get_channel(self):
        pass

    @abstractmethod
    def set_channel(self, channel):
        pass


class Color(ABC):
    @abstractmethod
    def apply(self):
        pass


class Blue(Color):
    def apply(self):
        return "blue"


class Red(Color):
    def apply(self):
        return "red"
