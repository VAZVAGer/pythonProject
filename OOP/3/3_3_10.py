class PolyLine:
    def __init__(self, start_coord, *args):
        self.start_coord = start_coord
        self.coord = args
        self.list_cord = [self.start_coord] + list(self.coord)

    def add_coord(self, x, y):
        self.list_cord.append((x, y))

    def remove_coord(self, indx):
        self.list_cord.pop(indx)

    def get_coords(self):
        return self.list_cord