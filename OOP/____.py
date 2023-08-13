lst_in = ['Системный блок: 1500 75890.56', 'Монитор Samsung: 2000 34000', 'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']  # list(map(str.strip, sys.stdin.readlines()))

def object_creator(list_in):
    list_obj = []
    for st in list_in:
        nam = st.split(":")
        nam1 = nam[-1].split()
        name = nam[0]
        weight = nam1[0]
        price = nam1[-1]
        list_obj.append(ShopItem(name, weight, price))
    return list_obj


object_creator(lst_in)

{<__main__.ShopItem object at 0x000001876A1B3490>: [<__main__.ShopItem object at 0x000001876A1B3490>, 0],
<__main__.ShopItem object at 0x000001876A1B3550>: [<__main__.ShopItem object at 0x000001876A1B36D0>, 1],
<__main__.ShopItem object at 0x000001876A1B3610>: [<__main__.ShopItem object at 0x000001876A1B3610>, 0]}

