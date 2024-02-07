class IteratorAttrs:
    def __iter__(self):
        for X in self.__dict__.items():
            yield X

class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self. memory = memory