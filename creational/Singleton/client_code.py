from creational.Singleton.singleton import Database


def singleton():
    foo = Database.get_instance()
    foo.query("SELECT * FROM usuarios")

    bar = Database.get_instance()
    bar.query("SELECT * FROM productos")

    # Verificamos que son la misma instancia
    print(f"¿Misma instancia? {foo is bar}")
