N = int(input())


def Balakirev_sequence():
    a, b, c = 1, 1, 1
    for i in range(N):
        if i < 1:
            yield 1
        else:
            a, b, c, = b, c, a + b + c
            yield a


d = Balakirev_sequence()
for i in d:
    print(i, end=" ")