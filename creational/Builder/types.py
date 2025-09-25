from enum import Enum


class Dough(Enum):
    THIN = "Masa delgada"
    TRADITIONAL = "Masa tradicional"
    THICK = "Masa gruesa"
    WHOLE_WHEAT = "Masa integral"
    GLUTEN_FREE = "Masa sin gluten"
    NEAPOLITAN = "Masa napolitana"
    DEEP_DISH = "Masa estilo Chicago"


class Sauce(Enum):
    TOMATO = "Salsa de tomate"
    MARINARA = "Salsa marinara"
    BBQ = "Salsa BBQ"
    ALFREDO = "Salsa Alfredo"
    PESTO = "Salsa pesto"
    GARLIC = "Salsa de ajo"
    WHITE = "Salsa blanca"
    BUFFALO = "Salsa buffalo"
    NO_SAUCE = "Sin salsa"


class Topping(Enum):
    # Quesos
    MOZZARELLA = "Mozzarella"
    PARMESAN = "Parmesano"
    CHEDDAR = "Cheddar"
    GORGONZOLA = "Gorgonzola"
    FETA = "Queso Feta"
    RICOTTA = "Ricotta"
    PROVOLONE = "Provolone"

    # Carnes
    PEPPERONI = "Pepperoni"
    HAM = "Jamón"
    BACON = "Tocino"
    CHICKEN = "Pollo"
    BEEF = "Carne de res"
    SAUSAGE = "Salchicha italiana"
    ANCHOVIES = "Anchoas"
    SALAMI = "Salami"
    MEATBALLS = "Albóndigas"

    # Vegetales
    MUSHROOMS = "Champiñones"
    BELL_PEPPERS = "Pimientos"
    ONIONS = "Cebollas"
    RED_ONIONS = "Cebollas moradas"
    OLIVES = "Aceitunas"
    TOMATOES = "Tomates frescos"
    PINEAPPLE = "Piña"
    SPINACH = "Espinacas"
    JALAPENOS = "Jalapeños"
    ARTICHOKES = "Alcachofas"
    ARUGULA = "Rúcula"
    CORN = "Maíz"

    # Hierbas y especiales
    BASIL = "Albahaca"
    CILANTRO = "Cilantro"
    GARLIC = "Ajo"
    OREGANO = "Orégano"
    CAPERS = "Alcaparras"
    ROSEMARY = "Romero"

    # Mariscos
    SHRIMP = "Camarones"
    CLAMS = "Almejas"
    TUNA = "Atún"
    SALMON = "Salmón"
