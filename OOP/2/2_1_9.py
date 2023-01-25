class ObjList:
    def __init__(self, next, prev, data, head=None, tail=None):
        self.__next = next
        self.__prev = prev
        self.__data = data
        self.head = head
        self.tail = tail

