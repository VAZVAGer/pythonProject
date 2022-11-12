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
        self.pole = empty_field

    def show(self):
        show_list = []
        for i in self.pole:
            for j in i:
                if j.fl_open == False:
                    show_list.append("#")
                elif j.fl_open == True and j.mine == True:
                    show_list.append("*")
                else:
                    show_list.append(self.around_mines)

        c = 0
        show_pole = [[0] * self.N for i in range(self.N)]
        for i in range(self.N):
            for j in range(self.N):
                show_pole[i][j] = show_list[c]
                c += 1
        print(*show_pole, sep="\n")

gp = GamePole(10, 12)
gp.init()
gp.show()
