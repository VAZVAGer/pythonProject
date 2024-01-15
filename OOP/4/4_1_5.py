class Thing:
    counter = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = Thing.counter
        Thing.counter += 1
        self.weight = None
        self.dims = None
        self.memory = None
        self.frm = None

    def get_data(self):
        return tuple(self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm)


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price, weight, dims)


class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price, memory, frm)
