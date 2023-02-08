class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, vel):
        if isinstance(vel, StackObj) or vel is None:
            self.__next = vel

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, vel):
        self.__data = vel


class Stack:
    def __init__(self):
        self.top = None
        self.lact = None
    def push(self, obj):
        if self.lact:
            self.lact.next = obj
        self.lact = obj
        if self.top is None:
            self.top = obj



    def pop(self):
        h = self.top
        if h is None:
            return
        while h and h.next != self.lact:
            h = h.next

        if h:
            h.next = None
        last = self.lact
        self.lact = h
        if self.lact is None:
            self.top = None
        return last


    def get_data(self):
        list_data = []
        h = self.top
        while h:
            list_data.append(h.data)
            h = h.next
        return list_data



s = Stack()
top = StackObj("obj_1")
s.push(top)
s.push(StackObj("obj_2"))
s.push(StackObj("obj_3"))
s.pop()

res = s.get_data()
assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"
assert s.top == top, "атрибут top объекта класса Stack содержит неверное значение"

h = s.top
while h:
    res = h.data
    h = h.next

s = Stack()
top = StackObj("obj_1")
s.push(top)
s.pop()
assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

n = 0
h = s.top
while h:
    h = h.next
    n += 1

assert n == 0, "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"

s = Stack()
top = StackObj("name_1")
s.push(top)
obj = s.pop()
assert obj == top, "метод pop() должен возвращать удаляемый объект"