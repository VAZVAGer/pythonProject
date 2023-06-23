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

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for i in other:
            self.push_back(StackObj(i))
        return self


assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"