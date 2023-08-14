import random


class DataBase:
    def __init__(self):
        self.dict_db = {}

    def write(self, record):
        pass

    def read(self, pk):
        pass


class Record:
    def __init__(self, fio, descr, old):
        self.fio = fio, self.descr = descr, self.old = old, self.pk = random.randint(0, 99999999)

    def __hash__(self):
        return hash(self.fio.lower()) + hash(self.old)

    def __eq__(self, other):
        return hash(self) == hash(other)


