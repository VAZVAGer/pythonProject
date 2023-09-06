import random


class Cell:
    def __init__(self):
        self.is_mine = False  # True - в клетке находится мина, False - мина отсутствует;
        self.number = 0  # число мин вокруг клетки (целое число от 0 до 8);
        self.is_open = True  # флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.

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
        if 0 <= vel <= 8:
            self.__number = vel
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        return self.__is_open

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
        self.__pole_cells = tuple(tuple(Cell() for _ in range(N)) for _ in range(M))
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
            x = random.randint(0, self.N)
            y = random.randint(0, self.M)
            if self.pole[x][y].is_mime == False:
                self.pole[x][y].is_mime = True
                count += 1
            else:
                continue

        indx = (-1, 1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for X in range(self.N):
            for Y in range(self.M):
                if not self.pole[X][Y].is_mine:
                    mines = sum((self.pole[X + i][Y + j].is_mine for i, j in indx if 0 <= X + i < self.N and 0 <= Y + j < self.M))
                    self.pole[X][Y].number = mines
