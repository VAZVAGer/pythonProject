# n, m = map(int, input().split())
# words = list(map(str, input().split()))
# lst_in = list(map(str.strip, sys.stdin.readlines()))
matrix = [8, 11, -53, 2, 10, 12]
mini = 0
mini_id = 0
for index_1, znachenie_1 in enumerate(matrix):
    print('znachenie_1', znachenie_1)

    for index_2, znachenie_2 in enumerate(matrix[index_1 : :]):
        print("znachenie_2", znachenie_2)

