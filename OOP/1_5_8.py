class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        vel = self.goods[indx]
        self.goods.remove(vel)

    def get_list(self):
        return ['<наименовние_1>: <цена_1>',
                '<наименовние_2>: <цена_2>',
                ...
                '<наименовние_N>: <цена_N>']


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price
