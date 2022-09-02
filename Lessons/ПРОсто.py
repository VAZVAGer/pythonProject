# n, m = map(int, input().split())
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# velue = list(map(int, input().split()))
s = "Главная Добавить Удалить Выйти"


def show_menu(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        n = 1
        for val in result:
            print(f'{n}.{val}')
            n += 1

    return wrapper


@show_menu
def get_list(s):
    lst_in = list(map(int, s.split()))
    return lst_in


get_menu(s)
