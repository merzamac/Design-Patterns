from abc import ABC, abstractmethod


class Data(ABC):
    @abstractmethod
    def load_data(self, file_path):
        pass
