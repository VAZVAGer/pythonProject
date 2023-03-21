class LineTo:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__y = y

class PathLines:
    def __init__(self, *args):
        self.coords = list((LineTo(0, 0),) + args)

