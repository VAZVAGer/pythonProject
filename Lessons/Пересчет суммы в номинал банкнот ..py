banknotes = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
Sum = int(input())
dupure_list = []
for nom in banknotes[::-1]:
    while Sum >= nom:
        if Sum >= nom and Sum - nom != nom:
            dupure_list.append(nom)
            Sum = Sum - nom

print(*dupure_list)