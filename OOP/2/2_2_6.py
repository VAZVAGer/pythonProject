class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, vel):
        if vel == None or vel == StackObj():
            self.__next = vel

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, vel):
        self.__data = vel


class Stack:
