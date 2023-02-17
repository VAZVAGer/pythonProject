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

    @classmethod
    def predict(cls, root, x):  ## x = [1, 1, 0]
        obj = root
        while obj.left != None or obj.right != None:
            if x[obj.self.indx] == 1:
                obj = obj.left
            else:
                obj = obj.right
        return obj

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.ridht = obj
            return obj
