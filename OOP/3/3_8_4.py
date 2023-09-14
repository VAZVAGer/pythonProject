class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if type(val) != int:
            raise ValueError('должно быть целое число')
        self.__value = val

    def __repr__(self):
        return str(self.__value)


class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.__cell = cell
        self.mas = [self.__cell() for _ in range(self.max_length)]
    def cheak_ind(self, ind):
        if type(ind) != int or not (-self.max_length <= ind < self.max_length):
             raise IndexError('неверный индекс для доступа к элементам массива')
    def __getitem__(self, item):
        self.cheak_ind(item)
        return self.mas[item].value

    def __setitem__(self, key, value):
        self.cheak_ind(key)
        self.mas[key].value = value

    def __repr__(self):
        return ' '.join(map(str, self.mas))


a = Array(20, cell=Integer)
assert a[18] == 0, "начальные значения в ячейках массива (в объектах класса Integer) должны быть равны 0"

a = Array(2, cell=Integer)
a[0] = 1
a[1] = 2
print(a)
assert str(a) == "1 2", "функция str(a) для объекта класса Array вернула неверное значение"
assert a[0] == 1 and a[1] == 2, "некорректно работает запись и/или считывание значений из массива по индексу"

try:
    a[1] = 2.5
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    a[100] = 25
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"