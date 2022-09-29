# list1 = list(map(int, input().split()))
# a, b = map(int, input().split())


def is_free(lst):
    return any('#' in x for x in lst)
