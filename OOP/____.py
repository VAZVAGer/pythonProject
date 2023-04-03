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
cells = [[0 for _ in range(M)] for _ in range(N)]
cells1 = [[0] * M] * N


print(cells)
print(cells1)

n = 1.0
for i in range(5):
    for j in range(3):
        cells[i][j] = n
        n += 1.0
n = 1.0
for i in range(5):
    for j in range(3):
        cells1[i][j] = n
        n += 1.0

print(cells)
print(cells1)
