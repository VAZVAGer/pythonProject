class Track:
    def __init__(self, start_x, start_y):
        self.__x = start_x
        self.__y = start_y
        self.point = []  #[[(start_x, start_y), 0]]

    def add_point(self, x, y, speed):
        self.point.append([(x, y), speed])

    def cheak_indx(self, ind):
        if type(ind) != ind and (0 <= ind < len(self.point)-1):
            raise IndexError('некорректный индекс')

    def __getitem__(self, item):
        self.cheak_indx(item)
        return self.point[item]

    def __setitem__(self, key, value):
        self.cheak_indx(key)
        self.point[key][-1] = value


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)
