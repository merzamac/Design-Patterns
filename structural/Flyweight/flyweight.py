class ChessPieceFlyweight:
    def __init__(self, name, color):
        self._color = color
        self._name = name

    def display(self, position):
        print(f"Displaying {self._color} {self._name} at {position}")
