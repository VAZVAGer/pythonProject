# n, m = map(int, input().split())
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# text = tuple(map(str, input().split()))


def get_nod(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


dd = get_nod(15, 121050)
print(dd)