from structural.Bridge.abstraction import (
    AdvancedRemoteControl,
    Circle,
    RemoteControl,
    Shape,
)
from structural.Bridge.concrete_implementations import Radio, Tv
from structural.Bridge.implementation import Blue, Color, Red


def client_code():
    tv = Tv()
    remote = RemoteControl(tv)
    remote.toggle_power()
    remote.volume_up()
    remote.channel_up()

    print("\n" + "=" * 40 + "\n")

    radio = Radio()
    advanced_remote = AdvancedRemoteControl(radio)
    advanced_remote.toggle_power()
    advanced_remote.volume_up()
    advanced_remote.mute()


def client_code2():
    circulo_blue = Circle(Blue(), 3)
    circulo_red = Circle(Red(), 5)

    print(circulo_red.draw())
    print(circulo_blue.draw())


def bridge():
    client_code2()
