import threading


class Database:
    # Campo estático para almacenar la instancia singleton
    _instance = None
    _lock = threading.Lock()  # Lock para thread safety

    # Constructor privado
    def __init__(self):
        # Algún código de inicialización
        # Por ejemplo, conexión a la base de datos
        print("Inicializando conexión a la base de datos...")
        # ...

    # Método estático que controla el acceso a la instancia singleton
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:  # Adquiere el lock automáticamente
                # Verifica nuevamente después de adquirir el lock
                if cls._instance is None:
                    cls._instance = Database()
        return cls._instance

    # Lógica de negocio
    def query(self, sql):
        # Lógica para ejecutar consultas
        print(f"Ejecutando consulta: {sql}")
        # Podría incluir throttling, caching, etc.
        # ...


"""from typing import Optional

from playwright.sync_api import Page


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class PageSingleton(metaclass=SingletonMeta):
    _page: Optional[Page] = None

    @classmethod
    def initialize(cls, page: Page) -> None:
        #Inicializar la página
        cls._page = page

    @classmethod
    def get_page(cls) -> Page:
        #Obtener la página almacenada
        if cls._page is None:
            raise ValueError(
                "Página no configurada. Usa PageSingleton.initialize(page) primero."
            )
        return cls._page
"""
