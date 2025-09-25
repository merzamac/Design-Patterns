from typing import Dict, List, Tuple

from structural.Flyweight.flyweight import ChessPieceFlyweight


class ChessPieceFactory:
    _chess_piece_types: Dict[Tuple[str, str], ChessPieceFlyweight] = {}

    @classmethod
    def get_flyweight(cls, name: str, color: str) -> ChessPieceFlyweight:
        key = (name.lower().strip(), color.lower().strip())
        if key not in cls._chess_piece_types:
            cls._chess_piece_types[key] = ChessPieceFlyweight(name, color)

        return cls._chess_piece_types[key]
