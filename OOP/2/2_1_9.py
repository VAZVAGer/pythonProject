class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self, ):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            new_Obj = ObjList(data)
            self.head = new_Obj
            return
        n = self.head
        while n.get_prev() is not None:
            n = n.get_prev()
        new_Obj = ObjList(data)
        n.set_prev = new_Obj
        new_Obj.set_prev = n
