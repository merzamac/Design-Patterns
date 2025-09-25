from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def delivery(self):
        pass
