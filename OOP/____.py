import random


def list_mines_random(N, M):
    object_list_mines = ['*'] * M
    object_list = ['#'] * ((N * N) - M)
    object_list = object_list + object_list_mines
    random.shuffle(object_list)
    print(object_list)
    c = 0
    B = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            B[i][j] = object_list[c]
            c += 1
    print(B)



list_mines_random(5, 5)



