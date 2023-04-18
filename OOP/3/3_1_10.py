class Mechanical:
    def __init__(self, date=0):
        self.date = date


class Aragon:
    def __init__(self, date=0):
        self.date = date


class Calcium:
    def __init__(self, date=0):
        self.date = date

    def __setattr__(self, key, value):
        if value == 0:
            object.__setattr__(self, key, value)


class GeyserClassic:
    MAX_DATE_FILTER = 100
    def __init__(self):
        filters = {}

