res = [[1, 2, 3, 4, 0],  # [[6, 8],
       [5, 6, 7, 8, 0],  # [9, 7]]
       [9, 8, 7, 6, 0],
       [5, 4, 3, 2, 0]]
size = (2, 2)
step = (2, 2)


def Max_Pooling(matrix):
    matrix_pattern = []
    list_values = []
    for ind_step_right in range(0, len(matrix[0]), step[-1]):
        matrix_pattern.append([])
        print(matrix_pattern)
        for ind_step_down in range(0, len(matrix), step[0]):
            sector = []
            if len(matrix[ind_step_down][ind_step_right:ind_step_right + size[0]]) != size[0]:
                matrix_pattern.pop()
                break
            else:
                sector.append(max(matrix[ind_step_down][ind_step_right:ind_step_right + size[0]]))   # первая строчка чектора
                for ind_size in range(ind_step_down + 1, size[-1] + ind_step_down): # последующие строки сектора
                    if ind_size < len(matrix):
                        sector.append(max(matrix[ind_size][ind_step_right:ind_step_right + size[0]]))

            if len(sector) == size[-1]:
                list_values.append(max(sector))
    print(matrix_pattern)

    counter = 0
    counter_2 = 0
    while counter_2 < len(list_values):
        counter += counter_2
        for ind, ls in enumerate(matrix_pattern):
            ls.append(list_values[counter_2])
            counter_2 += 1
    print(matrix_pattern)

























Max_Pooling(res)
