list = ["first", 1, 2, 3, "second", 10, 20, "pourth", -50]
# Надо создать словарь где слово это "ключ" а список чисел "значение"
my_dict = {}
kl = None
for www in list:
    if type(www) == str:
        zn = []
        kl = www
    elif type(www) == int:
        zn.append(www)
        my_dict[kl] = zn
print(my_dict)
