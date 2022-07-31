# n, m = map(int, input().split())
# words = list(map(str, input().split()))
# lst_in = list(map(str.strip, sys.stdin.readlines()))
matrix = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]
for ind_str, mea_str in enumerate(matrix):
    for ind_line, mea_line in enumerate(mea_str):
        if mea_line == 1:
            print(f'{mea_line} [{ind_str}][{ind_line}]')
            if matrix[ind_str - 1][ind_line - 1] == 0 and matrix[ind_str - 1][ind_line] == 0 and \
                    matrix[ind_str - 1][ind_line + 1] == 0 and matrix[ind_str][ind_line - 1] == 0 and \
                    matrix[ind_str][ind_line + 1] == 0 and matrix[ind_str + 1][ind_line - 1] == 0 and \
                    matrix[ind_str + 1][ind_line] == 0 and matrix[ind_str + 1][ind_line + 1] == 0:
                print('ДА')
            else:
                print('НЕТ')
