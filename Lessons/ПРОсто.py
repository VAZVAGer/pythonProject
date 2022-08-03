# n, m = map(int, input().split())
# words = list(map(str, input().split()))
# lst_in = list(map(str.strip, sys.stdin.readlines()))
matrix = [[2, 3, 4, 5, 6],
          [3, 2, 7, 8, 9],
          [4, 7, 2, 0, 4],
          [5, 8, 0, 2, 1],
          [6, 9, 4, 1, 2]]
answer = ""
for ind_str, mea_str in enumerate(matrix):
    for ind_line, mea_line in enumerate(mea_str):
        if matrix[ind_str][ind_line] == matrix[ind_line][ind_str]:
            answer = 'ДА'
        else:
            answer ="НЕТ"
print(answer)