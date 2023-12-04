class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        if self.value == 0:
            return True
        else:
            return False


class TicTacToe:
    SIZE = 3
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.init()

    def check_ibX(self, ind):
        X, Y = ind
        if not 0 <= X <= self.SIZE or not 0 <= Y <= self.SIZE:
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.check_ibX(item)
        X, Y = item
        return self.pole[X][Y].value

    def __setitem__(self, key, value):
        self.check_ibX(key)
        X, Y = key
        self.pole[X][Y].value = value


    def init(self):
        self.pole = tuple(tuple(Cell() for _ in range(self.SIZE)) for _ in range(self.SIZE))

    def show(self):
        self.show_pole = list(list([] for _ in range(self.SIZE)) for _ in range(self.SIZE))
        for line in self.pole:
            for zn in line:





