a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

c = list()
for d in b:
    if d in a:
        c.append(d)
print(c)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Выведите все элементы, которые меньше 5.
for m in a:
    if m < 5:
        print(m)

# Выведите первый и последний элемент списка.
print("Первый:", a[0], "последний:", a[-1])


# При заданном целом числе n посчитайте n + nn + nnn. 2+22+222=246
#def sum(n):
    #return n + (n * 11) + (n * 111)




print(sum(2))

# Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.
list_141 = [1, 2, 3, 458, 24, 46564, 554, 9254, 6584, 875587, 254, 8, 9, 9, 2, 7, 237, 996, 99, 4574, ]

for wv in list_141:
       if wv%2==0:
           print(wv)
       elif wv == 237:
           break


