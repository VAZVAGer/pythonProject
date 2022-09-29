# list1 = list(map(int, input().split()))
# a, b = map(int, input().split())

list1 = list(map(int, input().split()))
d = []
for zn in list1:
    if zn < 3:
        d.append(False)
    else:
        d.append(True)

rez = all(d)
if rez == True:
    print("учится")
else:
    print("отчислен")
