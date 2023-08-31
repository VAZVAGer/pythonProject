import random


class Cell:
    def __init__(self, is_mine=False, number=0, is_open=False):
        self.__is_mine = is_mine  # True - в клетке находится мина, False - мина отсутствует;
        self.__number = number  # число мин вокруг клетки (целое число от 0 до 8);
        self.__is_open = is_open  # флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, vel):
        if type(vel) == bool:
            self.__is_mine = vel
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, vel):
        if 0 <= vel <= 8:
            self.__number = vel
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        return self.__is_open

    def is_open(self, vel):
        if type(vel) == bool:
            self.__is_open = vel
        else:
            raise ValueError("недопустимое значение атрибута")


