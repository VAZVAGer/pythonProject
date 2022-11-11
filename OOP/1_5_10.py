import random


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False  # False-клетка закрыта/True-открыта


class GamePole:

    def __init__(self, N, M):
        self.N = N  # Размер поля
        self.M = M  # Общее число мин на поле.
        self.pole = []

    def init(self):
        parameter_list_mines = [True] * self.M
        parameter_list = [False] * ((self.N * self.N) - self.M)
        parameter_list = parameter_list + parameter_list_mines
        random.shuffle(parameter_list)
        for i, mine in enumerate(parameter_list):
            obj = Cell(0, mine)
            parameter_list.insert(i, obj)
            parameter_list.remove(mine)
        c = 0
        empty_field = [[0] * self.N for i in range(self.N)]
        for i in range(self.N):
            for j in range(self.N):
                empty_field[i][j] = parameter_list[c]
                c += 1
        print(empty_field)

    def show(self):
        print(self.pole)


gp = GamePole(2, 1)
gp.init()

