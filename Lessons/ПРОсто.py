# n, m = map(int, input().split())
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# text = tuple(map(str, input().split()))
def get_data_fig(*args, **kwargs):
    lst = []
    if "type" in kwargs or "color" in kwargs or 'closed' in kwargs or "width" in kwargs:
        for key, vel in kwargs.items():
            s = sum(args)
            lst.append(s)
            lst.append(vel)

        return tuple(lst)
    else:
        return sum(args)


d = [4, 5, 9, True]
print(*get_data_fig(*d))
