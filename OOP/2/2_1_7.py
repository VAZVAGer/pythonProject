class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, p1, p2):
        self.__sp = p1
        self.__ep = p2

    def __init__(self, x1, y1, x2, y2):
        self.__sp = Point(x1, y1)
        self.__ep = Point(x2, y2)
