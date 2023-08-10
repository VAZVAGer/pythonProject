class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    def __hash__(self):
        return hash(abs(self.width * self.height))
