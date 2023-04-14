# При заданном целом числе n посчитайте n + nn + nnn. 2+22+222=246

sp = []


def solve(n, a):
    for x in range(1, a + 1):
        m = int(str(n) * x)
        sp.append(m)


solve(2, 3)
print(sum(sp)) + int(b) + int(n)
