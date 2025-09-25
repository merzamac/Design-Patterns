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


class Tv(Device):
    def __init__(self):
        self.enabled = False
        self.volume = 50
        self.channel = 1

    def is_enabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True
        print("TV enabled")

    def disable(self):
        self.enabled = False
        print("TV disabled")

    def get_volume(self):
        return self.volume

    def set_volume(self, percent):
        self.volume = max(0, min(100, percent))
        print(f"TV volume set to {self.volume}")

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = max(1, channel)
        print(f"TV channel set to {self.channel}")


class Radio(Device):
    def __init__(self):
        self.enabled = False
        self.volume = 30
        self.channel = 88.0

    def is_enabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True
        print("Radio enabled")

    def disable(self):
        self.enabled = False
        print("Radio disabled")

    def get_volume(self):
        return self.volume

    def set_volume(self, percent):
        self.volume = max(0, min(100, percent))
        print(f"Radio volume set to {self.volume}")

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = max(87.5, channel)
        print(f"Radio channel set to {self.channel}")
