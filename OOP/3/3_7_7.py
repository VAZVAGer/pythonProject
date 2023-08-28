class Ellipse:
    def __init__(self, *args):
        self.args = args
        if args:
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]
    def __bool__(self):
        return bool(self.args)

    def get_coords(self):
        if len(self.args) > 0:
            return (self.x1, self.y1, self.x2, self.y2)

        else:
            raise AttributeError('нет координат для извлечения')


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 5, 7, 8), Ellipse(0, 9, 88, 4)]

for _ in lst_geom:
    if _:
        _.get_coords()





# class Ellipse:
#     def __init__(self, x1=None, y1=None, x2=None, y2=None):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#
#     def __bool__(self):
#         if self.x1 == self.x2 == self.y1 == self.y2 == None:
#             return False
#         else:
#             return True
#
#     def get_coords(self):
#         if self.x1 == self.x2 == self.y1 == self.y2 == None:
#             raise AttributeError('нет координат для извлечения')
#         else:
#             print(self.x1, self.y1, self.x2, self.y2)
#
#
# lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 5, 7, 8), Ellipse(0, 9, 88, 4)]
#
# for _ in lst_geom:
#     if _:
#         _.get_coords()