class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, val):
        if type(val) not in (int, float):
            raise ValueError("Неверный тип данных.")
        self.__real = val
    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, val):
        if type(val) not in (int, float):
            raise ValueError("Неверный тип данных.")
        self.__img = val

    def __abs__(self):
        return (self.__real * self.__real + self.__img * self.__img)**0.5

cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(c_abs)