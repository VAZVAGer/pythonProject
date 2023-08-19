class Deskript:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != int or type(value) != float:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(instance, self.name, value)
class Triangle:
    a = Deskript()
    b = Deskript()
    c = Deskript()

    def __init__(self, a, b, c):
        if a < b + c:
            self.a = a
        if b < a + c:
            self.b = b
        if c < b + a:
            self.c = c
