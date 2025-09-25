from structural.Decorator.component import Notifier, Text


class ConcretePlainText(Text):
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class Message(Notifier):
    def __init__(self, message):
        self._message = message

    def send(self):
        return self._message
