# list1 = list(map(int, input().split()))
# a, b = map(int, input().split())


# считывание списка из входного потока
lst_in = ['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']
di = {}
for zn in lst_in:
    lst = zn.split(":")
    di[int(lst[-1])] = lst[0]



def cheap(dict):
    ds = sorted(dict.items(), reverse=False)
    sr = ds[:3]
    for zn in sr:
        print(zn[-1], end=" ")


cheap(di)
