from structural.Facade.subsystem1 import InventorySystem
from structural.Facade.subsystem2 import PaymentProcessor
from structural.Facade.subsystem3 import ShipppingService


class OnlineStoreFacade:
    def __init__(self):
        self.inventory_system = InventorySystem()
        self.payment_processor = PaymentProcessor()
        self.shipping_service = ShipppingService()

    def place_order(self, user_id, product_id, quantity):
        if self.inventory_system.check_stock(
            product_id
        ) and self.payment_processor.process_payment(user_id, quantity):
            return self.shipping_service.check_shipping(user_id, product_id)
        else:
            return "Order failed"
