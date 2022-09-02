# n, m = map(int, input().split())
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# text = tuple(map(str, input().split()))
def get_data_fig(*args, **kwargs):
    s = sum(args)
    lst = [kwargs["type"], kwargs['color'], kwargs['closed'], kwargs['width']]
    if "type" not in kwargs:
        lst[0] = ''
    if "color" not in kwargs:
        lst[1] = ''
    if 'closed' not in kwargs:
        lst[2] = ''
    if 'width' not in kwargs:
        lst[3] = ''
    print(s, lst)


get_data_fig(15, 5, 3, color=25, type=True, closed=False)
