# list1 = list(map(int, input().split()))
# a, b = map(int, input().split())

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
di = {}
for zn in lst_in:
    lst = zn.split("=")
    di[int(lst[-1])] = lst[0]



def cheap(dict):
    ds = sorted(dict.items(),reverse=True)
    sr = ds
    for zn in sr:
        print(zn[-1], end=" ")
cheap(di)