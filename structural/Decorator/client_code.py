from structural.Decorator.component import Notifier
from structural.Decorator.concrete_component import Message
from structural.Decorator.concrete_decorator import (
    EmailDecorator,
    FacebookDecorator,
    SlakDecorator,
    SMSDecorator,
)


def client_code():
    message = Message("Esto es un mensaje")  #
    print(message.send())
    # vamos a decorar el mensaje
    SMSDecorator(message).send()
    FacebookDecorator(message).send()
    EmailDecorator(message).send()
    SlakDecorator(message).send()


def decorator():
    client_code()
