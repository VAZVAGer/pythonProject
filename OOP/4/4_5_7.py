from abc import ABC, abstractmethod


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):  ## добавление объекта в конец стека;
        return "абстрактный метод добавление объекта в конец стека"

    @abstractmethod
    def pop_back(self):  ## удаление последнего объекта из стека.
        return "абстрактный метод удаление последнего объекта из стека"


class Stack(StackInterface):
    def __init__(self):
        self._top = None
        self._last = self._top

    def push_back(self, obj):
        if self._top == None:
            self._top = self._last = obj
        else:
            self._last._next = obj
            self._last = obj

    def pop_back(self):
        ret = self._last
        _ = self._top
        while _._next != self._last:
            _ = self._._next
        self._last = _
        _ = None
        self._last._next = None
        return ret
class StackObj:
    def __init__(self, data):
        self._next = None
        self._data = data

assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"

try:
    a = StackInterface()
    a.pop_back()
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"


st = Stack()
assert st._top is None, "атрибут _top для пустого стека должен быть равен None"

obj_top = StackObj("obj")
st.push_back(obj_top)

assert st._top == obj_top, "неверное значение атрибута _top"

obj = StackObj("obj")
st.push_back(obj)

n = 0
h = st._top
while h:
    assert h._data == "obj", "неверные данные в объектах стека"
    h = h._next
    n += 1

assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

del_obj = st.pop_back()
assert del_obj == obj, "метод pop_back возвратил неверный объект"

del_obj = st.pop_back()
assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

assert st._top is None, "неверное значение атрибута _top"
