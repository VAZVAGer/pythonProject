class ListInteger(list):
    def cheak(self, value):
        if type(value) != int:
            raise TypeError('можно передавать только целочисленные значения')

    def __init__(self, value):
        for x in value:
            self.cheak(x)
        super().__init__(value)

    def __setitem__(self, key, value):
        self.cheak(value)
        super().__setitem__(key, value)

    def append(self, value):
        self.cheak(value)
        super().append(value)
