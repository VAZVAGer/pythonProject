class Dimensions:
    def __init__(self, a, b, c):
        if a <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        else:
            self.a = a
        if b <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        else:
            self.b = b
        if c <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        else:
            self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __eq__(self, other):
        return hash(self) == hash(other)
    def __lt__(self, other):
        return hash(self) < hash(other)


s_inp = "1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5"

lst_dims = []
spl_srt = s_inp.split(';')
for X in spl_srt:
    X = X.split()
    lst_dims.append(Dimensions(float(X[0]), float(X[1]), float(X[-1])))
lst_dims.sort()