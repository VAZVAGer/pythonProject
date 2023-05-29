class RadiusVector:
    def __init__(self, *args):
        self.cord = None
        if len(args) > 1:
            self.cord = args
        else:
            self.cord = (0,) * args[0]

    def set_coords(self, *args):
        self.cord = list(self.cord)
        for i, n in enumerate(args[:len(self.cord)]):
            self.cord[i] = n

    def get_coords(self):
        return self.cord

    def __len__(self):
        return len(self.cord)

    def __abs__(self):
        len_r = 0
        for i in self.cord:
            len_r += i * i
        return len_r ** 0.5


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
print(vector3D.set_coords(3, -5.6, 8, 10, 11))  # ошибки быть не должно, последние две координаты игнорируются
print(vector3D.set_coords(1, 2))  # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D)  # res_len = 3
res_abs = abs(vector3D)
print(res_len)
print(res_abs)
