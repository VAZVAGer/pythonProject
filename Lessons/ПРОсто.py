# list1 = list(map(int, input().split()))
# a, b = map(int, input().split())

list1 = list(map(float, input().split()))
list2 = []
for zn in list1:
    if zn < 0:
        list2.append(True)
    else:
        list2.append(False)

rezult = any(list2)
print(rezult)



