class Vector:
    def __init__(self, *args):
        self.cords = args

    def __add__(self, other):
        if len(self.cords) != len(other.cords):
            raise TypeError('размерности векторов не совпадают')
        new_list = []
        for nom, val in enumerate(self.cords):
            new_list.append(val + other.cords[nom])
        return Vector(*new_list)

    def __sub__(self, other):
        if len(self.cords) != len(other.cords):
            raise TypeError('размерности векторов не совпадают')
        new_list = []
        for nom, val in enumerate(self.cords):
            new_list.append(val - other.cords[nom])
        return Vector(*new_list)

    def get_coords(self):
        return tuple(self.cords)

class VectorInt(Vector):
    def __init__(self, *args):
        for val in args:
            if type(val) != int:
                raise ValueError('координаты должны быть целыми числами')
        self.cords = args

    def __add__(self, other):
        if len(self.cords) != len(other.cords):
            raise TypeError('размерности векторов не совпадают')
        new_list = []
        for nom, val in enumerate(self.cords):
            new_list.append(val + other.cords[nom])
        if type(other) == Vector:
            return Vector(*new_list)
        return VectorInt(*new_list)

    def __sub__(self, other):
        if len(self.cords) != len(other.cords):
            raise TypeError('размерности векторов не совпадают')
        new_list = []
        for nom, val in enumerate(self.cords):
            new_list.append(val - other.cords[nom])
        if type(other) == Vector:
            return Vector(*new_list)
        return VectorInt(*new_list)


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)

assert (v1 + v2).get_coords() == (
4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (
-2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1 + v2
assert type(
    v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1 + v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"