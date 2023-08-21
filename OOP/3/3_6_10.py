class Deskript:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) not in (int, float) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(instance, self.name, value)


class Triangle:
    a = Deskript()
    b = Deskript()
    c = Deskript()

    def __init__(self, a, b, c):
        if a >= b + c:
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        self.a = a

        if b >= a + c:
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        self.b = b
        if c >= b + a:
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        self.c = c

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self):
        p = (self.a + self.b + self.c) * 0.5
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"
