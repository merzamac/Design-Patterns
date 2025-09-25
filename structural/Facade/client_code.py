from structural.Facade.facade import OnlineStoreFacade


def client_code(facade: OnlineStoreFacade) -> None:
    print(facade.place_order("user1", "product1", 100))
    print(facade.place_order("user2", "product2", 200))


def facade():
    facade = OnlineStoreFacade()
    client_code(facade)
