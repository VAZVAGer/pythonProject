class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.last = None
        self.length = -1

    def push(self, obj):
        new_obj = obj
        if self.top == None and self.last == None:
            self.top = self.last = new_obj
        elif self.top == self.last:
            self.last = new_obj
            self.top.next = self.last
        else:
            self.last.next = new_obj
            self.last = new_obj
        self.length += 1

    def pop(self):
        ret = self.last
        counter = self.top
        while counter.next != self.last:
            counter = counter.next
        self.last = counter
        counter.next = None
        self.length -= 1
        return ret

    def check(self, indX):
        if type(indX) != int or indX < 0 or indX > self.length:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check(item)
        count = 0
        counter_obj = self.top
        if item == 0:
            return self.top
        else:
            while item > count:
                counter_obj = counter_obj.next
                count += 1
            return counter_obj

    def __setitem__(self, key, value):
        self.check(key)
        _ = self.top
        count = 0
        counter_obj = self.top
        if key == 0:
            _ = self.top.next
            self.top.next = None
            self.top = value
            self.top.next = _
        else:
            while key - 1 > count:
                counter_obj = counter_obj.next
                count += 1
            _1 = counter_obj.next
            _2 = _1.next
            counter_obj.next = None
            _1.next = None
            _1 = value
            counter_obj.next = _1
            _1.next = _2


st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
st[1] = StackObj("obj2-new")
assert st[0].data == "obj11" and st[
    1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st.pop()
assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

n = 0
h = st.top
while h:
    assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
    n += 1
    h = h.next

assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"
