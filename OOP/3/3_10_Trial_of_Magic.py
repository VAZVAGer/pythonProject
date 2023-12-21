import random


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
        for LINE in show_pole:
            print(LINE)
        return show_pole

    def human_go(self):
        self.show()
        cord = input(f"Введите координаты X и Y, от 0 до {self.SIZE} через пробел")
        d = cord.split()
        X = int(d[0])
        Y = int(d[-1])
        self[X, Y] = self.HUMAN_X
        self.show()

    def computer_go(self):
        walk = 0
        while walk == 0:
            random_X = random.uniform(0, self.SIZE)
            random_Y = random.uniform(0, self.SIZE)
            if self.pole[random_X][random_X] == self.FREE_CELL:
                self.pole[random_X][random_X] = self.COMPUTER_O
                walk = 8
        self.show()

    @property
    def is_human_win(self):
        show_pole = self.show()
        count_lict = []
        l = 0
        s = 0

        for line in show_pole:  # Перевіряемо строки
            if "0" not in line and " " not in line:
                print("True")
                return
            else:
                pass
        while s != len(show_pole):  # Перевіряємо стовпчики
            while l != len(show_pole):
                if show_pole[l][s] == 'X':
                    count_lict.append(True)
                else:
                    count_lict.append(False)
                l += 1
            s += 1
            l = 0
            if False not in count_lict:
                print("True")
                return
            count_lict = []
        for nom, line in enumerate(show_pole):  # Ліва діагональ
            if line[nom] == "X":
                count_lict.append(True)
            else:
                count_lict.append(False)
        if False not in count_lict:
            print("True")
            return
        count_lict = []
        for nom_maynas, line in enumerate(show_pole):  # Права діагональ
            if line[(nom_maynas * (-1)) - 1] == "X":
                count_lict.append(True)
            else:
                count_lict.append(False)
        if False not in count_lict:
            print("True")
            return

        print("False")
        return

    @property
    def is_computer_win(self):
        show_pole = self.show()
        count_lict = []
        l = 0
        s = 0

        for line in show_pole:  # Перевіряемо строки
            if "X" not in line and " " not in line:
                print("True")
                return
            else:
                pass
        while s != len(show_pole):  # Перевіряємо стовпчики
            while l != len(show_pole):
                if show_pole[l][s] == 'O':
                    count_lict.append(True)
                else:
                    count_lict.append(False)
                l += 1
            s += 1
            l = 0
            if False not in count_lict:
                print("True")
                return
            count_lict = []
        for nom, line in enumerate(show_pole):  # Ліва діагональ
            if line[nom] == "O":
                count_lict.append(True)
            else:
                count_lict.append(False)
        if False not in count_lict:
            print("True")
            return
        count_lict = []
        for nom_maynas, line in enumerate(show_pole):  # Права діагональ
            if line[(nom_maynas * (-1)) - 1] == "O":
                count_lict.append(True)
            else:
                count_lict.append(False)
        if False not in count_lict:
            print("True")
            return

        print("False")
        return

    @property
    def is_draw(self):
        if self.is_human_win == self.is_computer_win:
            return True
        else:
            return False

    def __bool__(self):
        if (self.is_human_win == False or self.is_computer_win == False) and self.show() in " ":
            return True
        else:
            return False
