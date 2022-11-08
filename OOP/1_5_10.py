class Cell:
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False  # False-клетка закрыта/True-открыта


class GamePole:

    def __init__(self, N, M):
        self.N = N  # Размер поля
        self.M = M  # Общее число мин на поле.
        self.pole = [['#' for i in range(N)] for j in range(N)]  #Создание пустого поля N*N

    def showe(self):
        print(self.pole)

gp = GamePole(3, 0)

gp.showe()
