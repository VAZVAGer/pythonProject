class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, data):
        self.__left = data

    @property
    def right(self):
        return self.__right

    @right.setter
    def left(self, data):
        self.__right = data


class DecisionTree:
    def __init__(self):
        self.head = None

    @classmethod
    def predict(cls, root, x):  ## x = [1, 1, 0]
        for ind, vel in enumerate(x):


    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if cls.head is None:
            new_obj = obj
            cls.head = new_obj
            return new_obj
        if left:
            node.left = obj
            return obj
        if left == False:
            node.ridht = obj
            return obj
