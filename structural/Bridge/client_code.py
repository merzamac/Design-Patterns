from structural.Bridge.abstraction import AdvancedRemoteControl, RemoteControl
from structural.Bridge.concrete_implementations import Radio, Tv


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


def bridge():
    client_code()
