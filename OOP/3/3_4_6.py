class StackObj:
    def __init__(self, txt):
        self.data = txt
        self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, vel):
        if type(vel) == str:
            self.__data = vel

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, vel):
        self.__next = vel


class Stack:
    def __init__(self):
        self.top = None

