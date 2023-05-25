class RadiusVector:
    def __init__(self, *args):
        self.cord = None
        if args[1]:
            self.cord = args
        else:
            self.cord = (0,) * args[0]

    def set_coords(self, *args):
        self.cord = args

    def get_coords(self):
        return self.cord

    def __len__(self):
        return len(self.cord)
    def __abs__(self):
        return