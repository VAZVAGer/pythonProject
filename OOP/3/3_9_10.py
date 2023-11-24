class Matrix:
    def cheack_list2D(self, list):
        for line in list:
            if len(line) != len(list):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            for element in list:
                if not isinstance(element, (int, float)):
                    raise TypeError('список должен быть прямоугольным, состоящим из чисел')


    def __init__(self, *args):
        if len(args) == 3:
            if type(args[0]) != int or type(args[1]) != int or isinstance(args[2], (int, float)):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.__rows = args[0]
            self.__cols = args[1]
            self.__matriX = list(list(args[2] for _ in range(self.__cols)) for _ in range(self.__rows))
        elif len(args) == 1:
            self.cheack_list2D(args)
            self.__matriX = [args]

    def __getitem__(self, item):
        ind1, ind2 = item
        if 0 > ind1 > len(self.__matriX) or 0 > ind2 > len(self.__matriX[ind1]):
            raise IndexError('недопустимые значения индексов')
        return self.__matriX[ind1][ind2]

    def __setitem__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')
        ind1, ind2 = key
        self.__matriX[ind1][ind2] = value

    def __eq__(self, other):
        return len(self) == len(other)

