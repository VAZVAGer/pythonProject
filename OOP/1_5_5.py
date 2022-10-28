class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not type(self.a) in (float, int) and self.a <= 0 and not type(self.b) in (
                float, int) and self.b <= 0 and not type(self.c) in (float, int) and self.c <= 0:
            return 1

        if self.a >= self.b + self.c or self.b >= self.a + self.c or self.c >= self.b + self.a:
            return 2
        else:
            return 3

#a, b, c = map(int, input().split())
tr = TriangleChecker(0, 4, 5)
print(tr.is_triangle())