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

    def get_path(self):
        return self.coords

    def get_length(self):  ##((x1-x0)**2 + (y1-y0)**2)**0,5
        summa = []
        l = 0
        while l + 1 < len(self.coords):
            value = (((self.coords[1 + l].x - self.coords[0 + l].x) ** 2) + (
                        (self.coords[1 + l].y - self.coords[0 + l].y) ** 2)) ** 0.5
            l += 1
            summa.append(value)
        return (sum(summa))

    def add_line(self, line):
        self.coords.append(line)


p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
