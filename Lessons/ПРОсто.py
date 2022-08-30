# n, m = map(int, input().split())
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# velue = list(map(int, input().split()))


def fib_rec(N, f=[]):
    if N >1000:
        N = 1000
    if f == []:
        f = [1, 1]
        N = N - 2
    f.append(f[-1] + f[-2])

    if N != 1:
        fib_rec(N - 1, f)
    return f

print(*fib_rec(2000))
