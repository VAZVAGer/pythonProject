# n, m = map(int, input().split())
# city = list(map(str, input().split()))
p = [0] * 10
input_number = 1

while input_number <= 10:
    list_element_index = int(input("Введите индекс элемента списка от 0 до 9:"))
    p[list_element_index] = 1
    input_number += 1
print(p)