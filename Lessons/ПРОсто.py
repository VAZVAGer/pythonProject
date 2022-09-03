# n, m = map(int, input().split())
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# velue = list(map(int, input().split()))


def sort(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        d = {result[0][0]: result[1][0], result[0][1]: result[1][1], result[0][2]: result[1][2],
             result[0][3]: result[1][3]}
        return d

    return wrapper


@sort
def get_list(s1, s2):
    lst_in1 = list(map(str, s1.split()))
    lst_in2 = list(map(str, s2.split()))
    lst_in3 = [lst_in1, lst_in2]
    return lst_in3


d = get_list(input(), input())
print(*sorted(d.items()))
