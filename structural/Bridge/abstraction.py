from structural.Bridge.implementation import Color


class RemoteControl:
    def __init__(self, device):
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_down(self):
        self.device.set_volume(self.device.get_volume() - 10)

    def volume_up(self):
        self.device.set_volume(self.device.get_volume() + 10)

    def channel_down(self):
        self.device.set_channel(self.device.get_channel() - 1)

    def channel_up(self):
        self.device.set_channel(self.device.get_channel() + 1)


# refined_abstraction.py optional
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self.device.set_volume(0)


class Shape:
    def __init__(self, color: Color):
        self.color = color

    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, color: Color, redius: int):
        super().__init__(color)
        self.radius = None

    def draw(self):
        return f"Círculo {self.color.apply()}"
