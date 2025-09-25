class Pizza:
    def __init__(self):
        self._dough = None
        self._sauce = None
        self._topping = None

    def __str__(self):
        toppings_str = ", ".join(self._topping)
        return f"Pizza con {self._dough}, {self._sauce}, y {toppings_str} topping."
