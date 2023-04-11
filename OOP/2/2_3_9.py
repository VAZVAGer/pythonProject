class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []
        self.weight = 0

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if thing.weight + self.weight < self.max_weight:
            self.__things.append(thing)
            self.weight = self.weight + thing.weight

    def remove_thing(self, indx):
        self.__things.pop(indx)

    def get_total_weight(self):
        return self.weight

class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight