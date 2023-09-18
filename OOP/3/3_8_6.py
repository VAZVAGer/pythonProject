class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None


class Stack:
    def __init__(self):
        self.top = None

    def c_obj(self):
        self.counter_obj = self.top
        while self.counter_obj.__next != None:
            self.counter_obj = self.counter_obj.__next
        return self.counter_obj

    def p_obj(self):
        self.penultimate_object = self.top
        while self.penultimate_object.__next != self.c_obj():
            self.penultimate_object = self.penultimate_object.__next
        return self.penultimate_object



    def push(self, obj):
        if self.top == None:
            self.top = obj
        elif self.top.__next == None:
            self.top.__next = obj
        else:
            self.c_obj(self).__next = obj

    def pop(self):
        if self.top.__next == None:
            self.top == None
        else:
            self.p_obj(self).__next == None


