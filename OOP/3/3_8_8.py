class Cell:
    def __init__(self):
        self.is_free = True  # True, если клетка свободна; False в противном случае;
        self.value = 0  # значение поля: 1 - крестик; 2 - нолик (по умолчанию 0).

    def __bool__(self):
        return self.is_free


class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def clear(self):
        for line in self.pole:
            for cell in line:
                cell.is_free = True
                cell.value = 0

    def check(self, val):
        if 0 > val[0] > 3 or 0 > val[1] > 3:
            raise IndexError('неверный индекс клетки')
        elif self.pole[val[0]][val[1]].is_free == False:
            raise ValueError('клетка уже занята')

    def __getitem__(self, item):
        self.check(item)
        return self.pole[item[0]][item[1]]

    def __setitem__(self, key, value):
        self.check(key)
        self.pole[key[0]][key[1]].value = value
