class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class StringValue:
    def __init__(self, min_length=2, max_length=50):
        self.min = min_length
        self.max = max_length

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == str and self.min <= len(value) <= self.max:
            setattr(instance, self.name, value)


class PriceValue:
    def __init__(self, max_value=10000):
        self.max = max_value

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == int or type(value) == float and 0 <= len(value) <= self.max:
            setattr(instance, self.name, value)

class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price
