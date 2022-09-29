# list1 = list(map(int, input().split()))
# a, b = map(int, input().split())

def is_string(lst):
    d = []
    for zn in lst:
        if type(zn) == str:
            d.append(True)
        else:
            d.append(False)
    return all(d)