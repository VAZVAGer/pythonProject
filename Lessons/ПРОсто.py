# list1 = list(map(int, input().split()))
# a, b = map(int, input().split())

lst_in = list(map(int, input().split()))
ss = set(lst_in)
lst = list(ss)
lst.sort(reverse=True)
print(*lst[:4])


