class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.__max_weight = max_weight
        self.bag = []
        self.weight_bag = 0

    def add_thing(self, thing):
        if (self.weight_bag + thing.weight) > self.__max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.bag.append(thing)
        self.weight_bag += thing.weight

    def chack(self, ind):
        if ind < 0 or ind > len(self.bag) - 1:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.chack(item)
        return self.bag[item]

    def __setitem__(self, key, value):
        old_object = self[key]
        if (self.weight_bag - old_object.weight + value.weight) > self.__max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.weight_bag = self.weight_bag - old_object.weight + value.weight
        self.chack(key)
        self.bag[key] = value


    def __delitem__(self, key):
        del self.bag[key]




b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"
