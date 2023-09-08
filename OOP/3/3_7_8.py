import random


class Cell:
    def __init__(self):
        self.is_mine = False  # True - в клетке находится мина, False - мина отсутствует;
        self.number = 0  # число мин вокруг клетки (целое число от 0 до 8);
        self.is_open = False  # флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, vel):
        if type(vel) == bool:
            self.__is_mine = vel
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, vel):
        if 0 <= vel < 8:
            self.__number = vel
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        return self.__is_open

    @is_mine.setter
    def is_open(self, vel):
        if type(vel) == bool:
            self.__is_open = vel
        else:
            raise ValueError("недопустимое значение атрибута")

    def __bool__(self):
        if self.is_open == True:
            return False
        elif self.is_open == False:
            return True


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.__pole_cells = tuple(tuple(Cell() for _ in range(M)) for _ in range(N))
        self.total_mines = total_mines

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(
            self):  # для инициализации начального состояния игрового поля (расставляет мины и делает все клетки закрытыми);
        for line in self.pole:
            for obj in line:
                obj.is_open = False
                obj.is_mine = False
        count = 0
        while count < self.total_mines:
            y = random.randint(0, self.M-1)
            x = random.randint(0, self.N-1)
            if self.pole[x][y].is_mine == False:
                self.pole[x][y].is_mine = True
                count += 1
            else:
                continue

        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for X in range(self.N):
            for Y in range(self.M):
                if not self.pole[X][Y].is_mine:
                    mines = sum((self.pole[X + i][Y + j].is_mine for i, j in indx if 0 <= X + i < self.N and 0 <= Y + j < self.M))
                    self.pole[X][Y].number = mines

    def open_cell(self, i, j):
        self.pole[i][j].is_open = True


p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)
assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1

cell = Cell()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
    Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

cell.is_mine = True
cell.number = 5
cell.is_open = True
assert bool(cell) == False, "функция bool() вернула неверное значение"

try:
    cell.is_mine = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    cell.number = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

p.init_pole()
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1

assert m == 10, "на поле расставлено неверное количество мин"
p.open_cell(0, 1)
p.open_cell(9, 19)

try:
    p.open_cell(10, 20)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


def count_mines(pole, i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                continue
            if pole[ii][jj].is_mine:
                n += 1

    return n


for i, row in enumerate(p.pole):
    for j, x in enumerate(row):
        if not p.pole[i][j].is_mine:
            m = count_mines(p.pole, i, j)
            assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"
