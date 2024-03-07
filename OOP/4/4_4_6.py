class Furniture:
    def __verify_name(self, name):
        if not type(name) == str:
            raise TypeError('название должно быть строкой')

    def __verify_weight(self, weight):
        if weight < 1:
            raise TypeError('вес должен быть положительным числом')

    def __init__(self, name, weight):
        self.__verify_name(name)
        self.__verify_weight(weight)
        self._name = name
        self._weight = weight


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return self.__dict__
class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height

    def get_attrs(self):
        return self.__dict_
class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self):
        return self.__dict_