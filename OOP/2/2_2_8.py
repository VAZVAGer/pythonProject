class TreeObj:
    def __init__(self, indx, value=None):
        self.__indx = indx
        self.__val = value
        self.__left = None
        self.__right = None


    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self,data):
        self.__left = data

    @property
    def ridht(self):
        return self.__right

    @ridht.setter
    def left(self, data):
        self.__right = data





