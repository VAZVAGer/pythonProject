class ObjList:
    def __init__(self, data=''):
        self.prev = None
        self.data = data
        self.next = None

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class LinkedList:
    def __init__(self):
        self.head = None  # ссылка на первый объект связного списка (если список пуст, то head = None)
        self.tail = None  # ссылка на последний объект связного списка (если список пуст, то tail = None)

    def __len__(self):
        counter = 0
        if self.head == None and self.tail == None:
            return 0
        else:
            ind_counter = self.head
            while ind_counter != None:
                ind_counter = ind_counter.next
                counter += 1
            else:
                return counter

    def __call__(self, ind, *args, **kwargs):
        if ind == 0:
            return self.head.data
        elif ind > 0:
            ind_counter = self.head
            counter = 0
            while counter != ind:
                ind_counter = ind_counter.next
                counter += 1
            else:
                if ind_counter is self.tail:
                    return self.tail.data
                else:
                    return ind_counter.data

    def add_obj(self, obj):
        if self.head == None and self.tail == None:
            self.head = obj
        elif self.head != None and self.tail == None:
            self.tail = obj
            obj.prev = self.head
            self.head.next = obj
        else:
            temporary_link = obj
            self.tail.next = obj
            temporary_link.prev = self.tail
            self.tail = obj

    def __get_obj_ind(self, ind):
        h = self.head
        n = 0
        while h and n < ind:
            h = h.next
            n += 1
        return h
    def remove_obj(self, ind):
        obj = self.__get_obj_ind(ind)
        if obj is None:
            return
        p, n = obj.prev, obj.next
        if p:
            p.next = n
        if n:
            n.prev = p
        if self.head == obj:
            self.head = n
        if self.tail == obj:
            self.tail = p

    # def remove_obj(self, ind):
    #     counter = 0
    #     if self.head != None and self.tail != None:
    #         if ind == 0 and self.tail is self.head.next:
    #             self.head = self.tail
    #             self.tail.prev = None
    #         if ind == 0 and self.head.next is not self.tail:
    #             self.head = self.head.next
    #             #self.head.prev = None
    #         if ind > 0:
    #             ind_counter = self.head
    #             while counter != ind:
    #                 ind_counter = ind_counter.next
    #                 counter += 1
    #             if ind_counter is not self.tail:
    #                 prev_object = ind_counter.prev
    #                 next_object = ind_counter.next
    #                 prev_object.next = next_object
    #                 next_object.prev = prev_object
    #             else:
    #                 self.tail = self.tail.prev
    #                 self.tail.next = None
    #
    #     else:
    #         print("Список пуст")

    # def remove_obj(self, ind):
    #     if ind == 0 and self.head.next is self.tail:
    #         self.head = self.tail
    #         self.tail.prev = None
    #     else:
    #         self.head = self.head.next
    #         if self.head is not None:
    #             self.head.prev = None
    #         if self.head is self.tail:
    #             self.tail = None
    #     if ind != 0:
    #         ind_counter = self.head
    #         counter = 0
    #         while counter != ind:
    #             ind_counter = ind_counter.next
    #             counter += 1
    #         if ind_counter is self.tail:
    #             if self.tail.prev is self.head:
    #                 self.tail = None
    #                 self.head.next = None
    #             self.tail = self.tail.prev
    #             self.tail.next = None
    #         else:
    #             prev_object = ind_counter.prev
    #             next_object = ind_counter.next
    #             prev_object.next = next_object
    #             next_object.prev = prev_object


ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert len(
    ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"
