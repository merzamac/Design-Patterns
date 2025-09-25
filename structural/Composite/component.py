from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    @abstractmethod
    def details(self):
        pass
