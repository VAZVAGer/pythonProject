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
        if type(val) == slice:
            return True
        elif 0 > val[0] > 3 or 0 > val[1] > 3:
            raise IndexError('неверный индекс клетки')
        elif self.pole[val[0]][val[1]].is_free == False:
            raise ValueError('клетка уже занята')

    def __getitem__(self, item):
        if type(item[0]) == type(item[1]):
            self.check(item)
            return self.pole[item[0]][item[1]].value
        else:
            if type(item[0]) == int:
                rez_l = []
                for _ in self.pole[item[0]]:
                    rez_l.append(_.value)
                return tuple(rez_l)

            elif type(item[1]) == int:
                rez = []
                for line in self.pole:
                    rez.append(line[item[1]].value)
                return tuple(rez)

    def __setitem__(self, key, value):
        self.check(key)
        self.pole[key[0]][key[1]].value = value


g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[
    2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"

g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3

assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (
    1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"
