def convert_to_preferred_format(sec):
    sec = sec % (24 * 3600)

    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    return f'часы:{hour}минуты:{min} секунды{sec}'


n = 10000
print(convert_to_preferred_format(n))
