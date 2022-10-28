class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all([type(self.a) in (float, int), type(self.b) in (float, int), type(self.c) in (float, int)]):
            return 1
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 1

        if self.a >= self.b + self.c or self.b >= self.a + self.c or self.c >= self.b + self.a:
            return 2
        else:
            return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(1, 5, 6)
print(tr.is_triangle())
