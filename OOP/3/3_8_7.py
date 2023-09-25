class RadiusVector:
    def __init__(self, *args):
        self.coords = args

    def __getitem__(self, item):
        if type(item) == int:
            return self.coords[item]
        elif type(item) == slice:
            return tuple(self.coords[item])

    def __setitem__(self, key, value):
        self.coords[key] = value


