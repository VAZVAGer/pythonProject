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
        self.pole = [['#' for i in range(N)] for j in range(N)]  # Создание пустого поля N*N

    def init(self):
        object_list_mines = [True] * self.M
        object_list = [False] * ((self.N * self.N) - self.M)
        object_list = object_list + object_list_mines
        random.shuffle(object_list)
        for mi in object_list:
            obj = Cell(0, mi)

    def showe(self):
        print(self.pole)




gp = GamePole(4, 0)

gp.showe()

