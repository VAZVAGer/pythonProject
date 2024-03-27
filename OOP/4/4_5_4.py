class ShopInterface:
    id_x = 0
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')

class ShopItem(ShopInterface):
    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self. __id = self.id_x + 1
        ShopInterface.id_x = self.__id
    def get_id(self):
        return self.__id