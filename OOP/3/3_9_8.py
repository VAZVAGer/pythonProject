import pytest


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.down = None
        self.N = 0

    def push_back(self, obj):  # для добавления нового объекта obj в конец стека
        if self.top == None and self.top == self.down:
            self.push_front(obj)
        else:
            _ = self.down
            self.down = obj
            _.next = self.down
            self.N += 1

    def push_front(self, obj):  # для добавления нового объекта obj в начало стека.
        if self.top == None and self.down == None:
            self.top = obj
            self.down = obj
            self.N += 1
        elif self.top == self.down and self.down != None:
            self.top = obj
            self.top.next = self.down
            self.N += 1
        else:
            _ = self.top.next
            self.top = obj
            self.top.next = _
            self.N += 1

    def __getitem__(self, item):
        if type(item) != int or not 0 <= item <= self.N - 1:
            raise IndexError('неверный индекс')
        elif item == 0:
            return self.top.data
        elif item == self.N - 1:
            return self.down.data
        else:
            count = 0
            _ = self.top
            while count != item:
                _ = self._.next
                count += 1
            return _.data

    def __setitem__(self, key, value):
        if type(key) != int or not (0 <= key <= self.N - 1):
            raise IndexError('неверный индекс')
        elif key == 0:
            self.top.data = value
        elif key == self.N - 1:
            self.down.data = value
        else:
            count = 0
            _ = self.top
            while count != key:
                _ = self._.next
                count += 1
            _.data = value

    def __len__(self):
        return self.N

    def __iter__(self):
        self._ = self.top
        return self

    def __next__(self):
        val = self._
        if self._.next != None:
            self._ = self._.next
        else:
            raise StopIteration
        return val


st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))
st.push_front(StackObj("2"))

assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
st[2] = "444"