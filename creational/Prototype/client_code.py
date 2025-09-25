from creational.Prototype.concrete_prototype import (
    Circle,
    Rectangle,
    SystemConfigPrototype,
)

# def prototype():
#     config = {
#         "resolution": "1920x1080",
#         "volume": 75,
#     }
#     system_config = SystemConfigPrototype(config)
#     cloned_config = system_config.clone()
#     print("Original Config:", system_config._configuration)
#     print("Cloned Config:", cloned_config._configuration)


def prototype():
    circle: Circle = Circle(10, 10)
    circle._radius = 20
    anotherCircle: Circle = circle.clone()

    rectangle: Rectangle = Rectangle(10, 10)
    rectangle._width = 20
    rectangle._height = 20
    anotherRectangle: Rectangle = rectangle.clone()

    print("Circles:", circle, anotherCircle, sep="\n")
    print("Rectangles:", rectangle, anotherRectangle, sep="\n")
