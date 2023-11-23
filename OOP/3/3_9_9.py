class Cell:
    def __init__(self, data=0):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, val):
        self.__data = val

class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.__type_data = type_data
        self.table = tuple(tuple(Cell() for _ in range(cols)) for _ in range(rows))
    def __cheack_index(self, index):
        r, c = index
        if not (0 <= r < self.rows) or not (0 <= c < self.cols):
            raise IndexError('неверный индекс')
    def __getitem__(self, item):
        self.__cheack_index(item)
        r, c = item
        return self.table[r][c].data

    def __setitem__(self, key, value):
        r, c = key
        self.__cheack_index(key)
        if type(value) != self.__type_data:
            raise TypeError('неверный тип присваиваемых данных')
        self.table[r][c].data = value

    def __iter__(self):
        for row in self.table:
            yield (x.data for x in row)

tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(
            value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"

assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"

tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"

try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"

try:
    a = tb[2, 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"