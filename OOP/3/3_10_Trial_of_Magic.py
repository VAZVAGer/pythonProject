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
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False

    def show(self):
        show_pole = list(list([] for _ in range(self.SIZE)) for _ in range(self.SIZE))
        for X, line in enumerate(self.pole):
            for Y, zn in enumerate(line):
                if zn.value == self.FREE_CELL:
                    show_pole[X][Y].append(" ")
                elif zn.value == self.HUMAN_X:
                    show_pole[X][Y].append("X")
                elif zn.value == self.COMPUTER_O:
                    show_pole[X][Y].append("O")
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
            if ["0"] not in line and [" "] not in line:

                return True
            else:
                pass
        while s != len(show_pole):  # Перевіряємо стовпчики
            while l != len(show_pole):
                if show_pole[l][s] == ['X']:
                    count_lict.append(True)
                else:
                    count_lict.append(False)
                l += 1
            s += 1
            l = 0
            if False not in count_lict:

                return True
            count_lict = []
        for nom, line in enumerate(show_pole):  # Ліва діагональ
            if line[nom] == ["X"]:
                count_lict.append(True)
            else:
                count_lict.append(False)
        if False not in count_lict:
            return True
        count_lict = []
        for nom_maynas, line in enumerate(show_pole):  # Права діагональ
            if line[(nom_maynas * (-1)) - 1] == ["X"]:
                count_lict.append(True)
            else:
                count_lict.append(False)
        if False not in count_lict:
            return True

        return False
    @is_human_win.setter
    def is_human_win(self, value):
        return value

    @property
    def is_computer_win(self):
        show_pole = self.show()
        count_lict = []
        l = 0
        s = 0

        for line in show_pole:  # Перевіряемо строки
            if ["X"] not in line and [" "] not in line:

                return True
            else:
                pass
        while s != len(show_pole):  # Перевіряємо стовпчики
            while l != len(show_pole):
                if show_pole[l][s] == ['O']:
                    count_lict.append(True)
                else:
                    count_lict.append(False)
                l += 1
            s += 1
            l = 0
            if False not in count_lict:

                return True
            count_lict = []
        for nom, line in enumerate(show_pole):  # Ліва діагональ
            if line[nom] == ["O"]:
                count_lict.append(True)
            else:
                count_lict.append(False)
        if False not in count_lict:
            return True
        count_lict = []
        for nom_maynas, line in enumerate(show_pole):  # Права діагональ
            if line[(nom_maynas * (-1)) - 1] == ["O"]:
                count_lict.append(True)
            else:
                count_lict.append(False)
        if False not in count_lict:
            return True


        return False
    @is_computer_win.setter
    def is_computer_win(self, value):
        return value


    @property
    def is_draw(self):
        if self.is_human_win == self.is_computer_win == True:
            return True
        else:
            return False
    @is_draw.setter
    def is_draw(self, value):
        return value
    def __bool__(self):
        for line in self.show():
            if [" "] in line:
                QQ = True
        if (self.is_human_win == False and self.is_computer_win == False) and QQ == True:
            return True
        else:
            return False


cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe,
                                                                                 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[
           0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[
    1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
