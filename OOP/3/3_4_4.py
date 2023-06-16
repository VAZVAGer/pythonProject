class NewList:
    def __init__(self, lst=[]):
        if type(lst) == list:
            self.lst = lst

    def subtraction(self, lst1, lst2):
        sub_list = []
        work_list = lst1.copy()
        work_list2 = lst2.copy()
        for i, zn1 in enumerate(lst1):
            flag = []
            for ii, zn2 in enumerate(work_list2):
                flag.append(type(zn1) == type(zn2) and zn1 == zn2)
                if type(zn1) == type(zn2) and zn1 == zn2:
                    work_list2[ii] = None
                    break

            if True not in flag:
                sub_list.append(zn1)
        return sub_list

    def __sub__(self, other):
        if type(other) is NewList:
            return NewList(self.subtraction(self.lst, other.lst))
        elif type(other) == list:
            return NewList(self.subtraction(self.lst, other))

    def __rsub__(self, other):
        if type(other) is NewList:
            return NewList(self.subtraction(other.lst, self.lst))
        elif type(other) == list:
            return NewList(self.subtraction(other, self.lst))



    def get_list(self):
        return self.lst


lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])

assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"

res1 = lst1 - lst2
res2 = lst1 - [0, True]
res3 = [1, 2, 3, 4.5] - lst2
lst1 -= lst2
assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87]) #0, 5.0,
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"
