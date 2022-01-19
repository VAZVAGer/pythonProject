total = 0  # переменная АКБ
for p in range(1, 5):
    total += p

print(total)

total_1 = 0  # переменная АКБ_1
p_1 = 0  # переменная счетчик
while p_1 < 5:  # условие цикла
    total_1 += p_1
    p_1 += 1
print(total_1)

my_list = [9, 7, 4, 3, 1, 0, -2, -7, -15]
# надо найти  сумму положительный чисал в списке
total2 = 0
p2 = 0
while my_list[p2] > 0:
    total2 += my_list[p2]
    p2 += 1
print(total2)

my_list2 = [9, 7, 4, 3, 1, ]
# надо найти  сумму положительный чисал в списке
total3 = 0
p3 = 0
while p3 < len(my_list2) and my_list2[p3] > 0:
    total3 += my_list2[p3]
    p3 += 1
print(total2)

p6 = 0
while 1 < 2:
    if p6 == 10:
        break
    print(p6)
    p6 += 1

