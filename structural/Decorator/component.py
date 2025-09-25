from abc import ABC, abstractmethod


class Text(ABC):
    @abstractmethod
    def render(self):
        pass


class Notifier(ABC):
    @abstractmethod
    def send(self):
        pass
