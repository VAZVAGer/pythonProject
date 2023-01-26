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

    def add_obj(self, obj):
        if self.head is None:
            self.head = obj
            return
        n = self.head
        while n.get_prev is not None:
            n = n.get_prev()
        n.set_prev = obj
        obj.set_prev = n

