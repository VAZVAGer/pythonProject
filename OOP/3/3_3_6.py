class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, val):
        if val in (int, float):
            self.__real = val
    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, val):
        if val in (int, float):
            self.__img = val

    def __abs__(self):
        return abs((self.real * self.real + self.img * self.img)**0.5)