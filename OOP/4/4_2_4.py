class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash(self.name) + hash(self.price) + hash(self.weight)


class DictShop(dict):
    def __init__(self, things=None):
        if things == None:
            self.things = {}
        else:
            self.things = things
        if not isinstance(self.things, dict):
            raise TypeError('аргумент должен быть словарем')
        if self.things and not all(isinstance(key, Thing) for key in self.things):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__init__(self.things)

    def __setitem__(self, key, value):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key, value)
