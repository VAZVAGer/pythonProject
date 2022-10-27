import random


class Line:
    def _init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def _init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def _init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


a, b, c, d = random.sample(range(0, 101), 4)
elements = [random.choice([Line, Rect, Ellipse])(a, b, c, d) for n in range(217)]

for obj in elements:
    if isinstance(obj, Line):
        obj.sp = obj.ep = 0, 0