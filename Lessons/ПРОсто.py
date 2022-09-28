# list1 = list(map(int, input().split()))
# a, b = map(int, input().split())

def get_list_dig(lst):
    lst2 = []
    for zn in lst:
        if type(zn) in (int, float):
            lst2.append(zn)
    return lst2
