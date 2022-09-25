# list1 = list(map(int, input().split()))
# a, b = map(int, input().split())


d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
def get_sort(d):
    ds = dict(sorted(d.items(), reverse=True))
    return [*ds.values()]

get_sort(d)