# list1 = list(map(int, input().split()))
# a, b = map(int, input().split())

lst_in = ['Номер;Имя;Оценка;Зачет', '1;Портос;5;Да', '2;Арамис;3;Да', '3;Атос;4;Да', "4;д'Артаньян;2;Нет",
          '5;Балакирев;1;Нет']
lst_in2 = []
for zn in lst_in:
    a = zn.split(";")
    try:
        a[0] = int(a[0])
        a[2] = int(a[2])
    except:
        pass
    lst_in2.append(a)
print(lst_in2)

