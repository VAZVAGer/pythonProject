class NewList:
    def __init__(self, lst=[]):
        if type(lst) == list:
            self.lst = lst

    @classmethod
    def subtraction(als, lst1, lst2):
        list_sub = []
        for i in lst1:
            if i in lst2:
                lst2.remove(i)
            else:
                list_sub.append(i)
        return list_sub

    def __sub__(self, other):
        if type(other) is NewList:
            return NewList.subtraction(self.lst, other.self.lst)
        elif type(other) == list:
            return NewList.subtraction(self.lst, other)
