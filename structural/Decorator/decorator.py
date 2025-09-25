from structural.Decorator.component import Notifier, Text
from structural.Decorator.concrete_component import Message


class TextDecorator(Text):
    def __init__(self, text_component) -> None:
        self._text_component = text_component

    def render(self):
        return self._text_component.render()


class BaseDecorator(Notifier):
    def __init__(self, sender: Message) -> None:
        self._sender: Message = sender

    def send(self):
        """Envía el mensaje a través del notificador envuelto"""
        return self._sender.send()
