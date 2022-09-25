# list1 = list(map(int, input().split()))
# a, b = map(int, input().split())

s = 'Python дай мне силы пройти этот курс до конца!'
N = []
lst = []
for n, i in enumerate(s):
    if n < 10:
        N.append(n)
zi = zip(s, N)
for i in zi:
    lst.append(i)
print(lst)

def myCoolAlg():
    return 1