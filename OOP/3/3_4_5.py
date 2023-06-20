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