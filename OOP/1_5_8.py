class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        vel = self.goods[indx]
        self.goods.remove(vel)

    def get_list(self):
        print([f'{x.name}: {x.price}' for x in self.goods])


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


cart = Cart()
cart.add(TV("LG", 1200))
cart.add(TV("Samsung", 18000))
cart.add(Table("Кухонный", 1600))
cart.add(Notebook('Asus', 77000))
cart.add(Notebook("Asus", 96500))
cart.add(Cup("Из нержи", 50))

cart.get_list()
