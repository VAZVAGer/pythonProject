class ListMath:
    def __init__(self, lst=None):
        if lst == None:
            self.lst_math = []
        elif type(lst) == list:
            self.lst_math = []
            for zn in lst:
                if isinstance(zn, int | float):
                    self.lst_math.append(zn)

    def __add__(self, other):
        work_list = self.lst_math
        for i, zn in enumerate(work_list):
            work_list[i] += other
        return ListMath(work_list)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        for i, zn in enumerate(self.lst_math):
            self.lst_math[i] += other
        return self

    def __sub__(self, other):
        work_list = self.lst_math
        for i, zn in enumerate(work_list):
            work_list[i] -= other
        return ListMath(work_list)

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        for i, zn in enumerate(self.lst_math):
            self.lst_math[i] -= other
        return self

    def __mul__(self, other):
        work_list = self.lst_math
        for i, zn in enumerate(work_list):
            work_list[i] *= other
        return ListMath(work_list)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        for i, zn in enumerate(self.lst_math):
            self.lst_math[i] *= other
        return self

    def __truediv__(self, other):
        work_list = self.lst_math
        for i, zn in enumerate(work_list):
            work_list[i] /= other
        return ListMath(work_list)

    def __rtruediv__(self, other):
        return self / other

    def __itruediv__(self, other):
        for i, zn in enumerate(self.lst_math):
            self.lst_math[i] /= other
        return self