class ObjList:
    def __init__(self, prev=None, data='', next=None):
        self.prev = prev
        self.data = data
        self.next = next

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

    def remove_obj(self,
                   ind):  # удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); индекс отсчитывается с нуля.
        if ind == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            ind_counter = self.head
            counter = 0
            while counter != ind:
                ind_counter = ind_counter.next
                counter += 1
            else:
                prev_object = ind_counter.prev
                next_object = ind_counter.next
                prev_object.next = ind_counter.next
                next_object.prev = ind_counter.prev
