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
        show_pole = list(list([] for _ in range(self.SIZE)) for _ in range(self.SIZE))
        for X, line in enumerate(self.pole):
            for Y, zn in enumerate(line):
                if zn.value == self.FREE_CELL:
                    show_pole[X][Y].append(" ")
                elif zn.value == self.HUMAN_X:
                    show_pole[X][Y].append("X")
                elif zn.value == self.COMPUTER_O:
                    show_pole[X][Y].append("0")
        print(show_pole)
    def human_go(self):
        cord = input(f"Введите координаты X и Y, от 0 до {self.SIZE} через пробез")
        d = cord.split()
        X = int(d[0])
        Y = int(d[-1])








