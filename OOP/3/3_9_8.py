class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None


class Stack:
    def __init__(self):
        self.top = None
        self.down = None

    def push_back(self, obj):  # для добавления нового объекта obj в конец стека
        if self.top == None and self.top == self.down:
            self.push_front(obj)
        else:
            _ = self.down
            self.down = obj
            _.__next = self.down

    def push_front(self, obj):  # для добавления нового объекта obj в начало стека.
        if self.top == None and self.down == None:
            self.top = obj
            self.down = self.top
        elif self.top == self.down and self.down != None:
            self.top = obj
            self.top.__next = self.down
        else:
            _ = self.top.__next
            self.top = obj
            self.top.__next = _
