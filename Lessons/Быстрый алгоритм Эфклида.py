def get_nod(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

dd = get_nod(15, 121050)
print(dd)
