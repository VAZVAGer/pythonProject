import sys


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash(self.name.lower()) + hash(self.weight) + hash(self.price)

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = ['Системный блок: 1500 75890.56', 'Монитор Samsung: 2000 34000', 'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']  # list(map(str.strip, sys.stdin.readlines()))
shop_items = {}


def object_creator(list_in):
    list_obj = []
    for st in list_in:
        nam = st.split(":")
        nam1 = nam[-1].split()
        name = nam[0]
        weight = nam1[0]
        price = nam1[-1]
        list_obj.append(ShopItem(name, weight, price))
    for odj in list_obj:
        counter_of_identical_objects = 0
        for odj2 in list_obj:
            if odj == odj2:
                counter_of_identical_objects += 1
        shop_items[odj] = [odj, counter_of_identical_objects]



object_creator(lst_in)

it1 = ShopItem('name', 10, 11)
it2 = ShopItem('name', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

it2 = ShopItem('name', 10, 12)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('name', 11, 11)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('NAME', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

name = lst_in[0].split(':')
for sp in shop_items.values():
    assert isinstance(sp[0], ShopItem) and type(sp[
                                                    1]) == int, "в значениях словаря shop_items первый элемент должен быть объектом класса ShopItem, а второй - целым числом"

v = list(shop_items.values())


if v[0][0].name.strip() == "Системный блок":
    assert v[0][1] == 1 and v[1][1] == 2 and v[2][1] == 1 and len(v) == 3, "неверные значения в словаре shop_items"

if v[0][0].name.strip() == "X-box":
    assert v[0][1] == 2 and v[1][1] == 1 and v[2][1] == 2 and len(v) == 3, "неверные значения в словаре shop_items"
