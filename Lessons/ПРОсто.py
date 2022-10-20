# list1 = list(map(int, input().split()))
# a, b = map(int, input().split())

import random
import numpy as np  # импортируем в задачу модуль
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
N = 10
P = [[0] * N for i in range(N)]

# здесь продолжайте программу
# функция проверяет что соседние клетки не содержат 1
def is_isolate(i, j):
    return sum([P[i - 1][j - 1], P[i - 1][j], P[i - 1][j + 1],
                P[i][j - 1], P[i][j + 1], P[i + 1][j - 1],
                P[i + 1][j], P[i + 1][j + 1]]) == 0


# строим границу из нулей вокруг матрицы P
P = np.pad(P, pad_width=1, mode='constant', constant_values=0)

# Заполняем поле 10-ю минами
for _ in range(10):
    while True:
        # генерируем координаты ячейки пока не найдём свободную от 1 и с 0 вокруг
        row = random.randint(1, N - 3)  # при N - 2 время не хватит для решения
        column = random.randint(1, N - 2)
        # если ячейка свободная, то занимаем её
        if is_isolate(row, column) and P[row][column] != 1:
            P[row][column] = 1
            break