lst = list(map(int, input().split()))
n = int(len(lst)**0.5)
print(n)
print([lst[x:x+n] for x in range(0, len(lst), n)])