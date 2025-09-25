from structural.Flyweight.factory import ChessPieceFactory
from structural.Flyweight.flyweight import ChessPieceFlyweight


def client_code():
    king_black_flyweight: ChessPieceFlyweight = ChessPieceFactory.get_flyweight(
        "king", "black"
    )

    # Verificar que es el mismo objeto (debería ser True)
    same_flyweight: ChessPieceFlyweight = ChessPieceFactory.get_flyweight(
        "king", "black"
    )
    same_flyweight.display("A1")
    king_black_flyweight.display("B1")

    print(
        "Are they the same flyweight?", king_black_flyweight is same_flyweight
    )  # True


def flyweight():
    client_code()
