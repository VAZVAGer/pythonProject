tuple1 = tuple(map(int, input().split()))
list_zn = []
list_ind = []
for ind, zn in enumerate(tuple1):
    if tuple1.count(zn) > 1:
        list_ind.append(ind)
print(*list_ind)