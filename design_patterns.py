from creational.AbstractFactory.client_code import abstract
from creational.Builder.client_code import builder
from creational.FactoryMethod.client_code import factory
from creational.Prototype.client_code import prototype
from creational.Singleton.client_code import singleton
from structural.Adapter.client_code import adapter
from structural.Bridge.client_code import bridge
from structural.Composite.client_code import composite
from structural.Decorator.client_code import decorator
from structural.Facade.client_code import facade
from structural.Flyweight.client_code import flyweight


class StructuralPatterns:
    @property
    def adapter(self):
        adapter()

    @property
    def decorator(self):
        decorator()

    @property
    def facade(self):
        facade()

    @property
    def composite(self):
        composite()

    @property
    def flyweight(self):
        flyweight()

    @property
    def bridge(self):
        bridge()


class Behavioral_Patterns:
    pass


class CreationalPatterns:
    @property
    def factory_method(self):
        factory()

    @property
    def abstract_factory(self):
        abstract()

    @property
    def builder(self):
        builder()

    @property
    def prototype(self):
        prototype()

    @property
    def singleton(self):
        singleton()
