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
        if self.weight_bag + thing.weight > self.__max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.bag.append(thing)
        self.weight_bag += thing.weight



