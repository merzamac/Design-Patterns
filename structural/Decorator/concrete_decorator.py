from structural.Decorator.decorator import BaseDecorator, TextDecorator


class ConcreteTextDecorator(TextDecorator):
    def render(self):
        return f"<p>{self._text_component.render()}</p>"


class SMSDecorator(BaseDecorator):
    def send(self):
        print(f"Decorado con SMS: {self._sender.send()}")


class FacebookDecorator(BaseDecorator):
    def send(self):
        print(f"Decorado con Facebook: {self._sender.send()}")


class EmailDecorator(BaseDecorator):
    def send(self):
        print(f"Decorado con Email: {self._sender.send()}")


class SlakDecorator(BaseDecorator):
    def send(self):
        print(f"Decorado con Slack: {self._sender.send()}")
