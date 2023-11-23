class Matrix:
    def __init__(self, *args):
        if len(args) == 3:
            if type(args[0]) != int or type(args[1]) != int or isinstance(args[2], (int, float)):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.__rows = args[0]
            self.__cols = args[1]
            self.__matriX = list(list(args[2] for _ in range(self.__cols)) for _ in range(self.__rows))
        elif len(args) == 1:
            self.__matriX = args
