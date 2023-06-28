class XXX:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


a1 = XXX(1, 8, 3)
a2 = XXX(5, 8, 3)
a3 = XXX(1, 8, 3)

print(a1 is a3)