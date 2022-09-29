# list1 = list(map(int, input().split()))
# a, b = map(int, input().split())

list1 = list(map(int, input().split()))
list2 = []
for zn in list1:
    if zn % 2 == 0:
        list2.append(True)
    else:
        list2.append(False)

rezult = all(list2)
print(rezult)