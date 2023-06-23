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
        self.end = None

    def push_back(self, obj):  # Добавление в список
        if self.top == None:
            self.top = obj
            self.end = obj
        else:
            self.end.next = obj
            self.end = obj

    def pop_back(self):  # удаление из списка
        counter = self.top
        while counter.next != self.end:
            counter = counter.next
        self.end = counter
        counter.next = None

