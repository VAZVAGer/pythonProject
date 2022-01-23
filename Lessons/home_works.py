# Домашка. Надо найти сумму отрицаткльных чисел , начиная с конца списка.
my_home_list = [9, 7, 4, 3, 1, 0 - 1, -3, -8, -12, -20]
total_home = 0
p_home = -1
while my_home_list[p_home] < 0:
    total_home += my_home_list[p_home]
    p_home += -1
print(total_home)
# Тоже самое только методом for
total_home_if = 0

for i in my_home_list:
    if i <= 0:
        total_home_if += i
print(total_home_if)

# Надо из списка вывести все значения до "СТОП" не выводя его.
my_home_list_1 = ["Дом", "сад", "мед", "карантин", "stop", "попкорн", "ручка"]
for i2 in my_home_list_1:
    if i2 == "stop":
        break
    print(i2)
print("!!!!!Метод фор работает!!!!")
# Тоже самое только методом While
i3=0
while my_home_list_1[i3] != "stop":
    print(my_home_list_1[i3])
    i3+=1

print ("Eсли ты видешь только это, значит метод не работает")