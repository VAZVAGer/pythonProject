class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    # body1 > body2  # True, если масса тела body1 больше массы тела body2
    # body1 == body2 # True, если масса тела body1 равна массе тела body2
    # body1 < 10     # True, если масса тела body1 меньше 10
    # body2 == 5     # True, если масса тела body2 равна 5
    def __eq__(self, other):
        if type(other) == int:
            return self.ro * self.volume == other
        return self.ro * self.volume == other.ro * other.volume

    def __lt__(self, other):
        if type(other) == int:
            return self.ro * self.volume < other
        return self.ro * self.volume < other.ro * other.volume
