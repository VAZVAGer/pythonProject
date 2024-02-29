class ItemAttrs:
    def __init__(self, X, Y):
        self.cord = [X, Y]

    def __getitem__(self, items):
        return self.cord[items]

    def __setitem__(self, key, value):
        self.cord[key] = value


class Point(ItemAttrs):
    def __init__(self, X, Y):
        super().__init__(X, Y)


pt = Point(1, 2.5)
x = pt[0]  # 1
y = pt[1]  # 2.5
pt[0] = 10
