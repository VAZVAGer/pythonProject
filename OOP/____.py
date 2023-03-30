class FloatValue:

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __set__(self, instance, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value
N = 5
M = 3
cells = [[Cell() for _ in range(M)] for _ in range(N)]
cells1 = [[Cell()] * M] * N
print(cells)
print(cells1)