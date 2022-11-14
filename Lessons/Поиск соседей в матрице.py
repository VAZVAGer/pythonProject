matrix = [[1, 0, 0, 0, 0],
          [0, 0, 1, 0, 1],
          [0, 0, 0, 0, 0],
          [0, 1, 0, 1, 0],
          [0, 0, 0, 0, 0]]
list_of_neighbors = []
for ind_str, mea_str in enumerate(matrix):
    for ind_line, mea_line in enumerate(mea_str):
        if mea_line == 1:
            try:
                if ind_str - 1 == -1 or ind_line - 1 == -1:
                    pass
                else:
                    list_of_neighbors.append(matrix[ind_str - 1][ind_line - 1])
            except:
                pass
            try:
                if ind_str - 1 == -1 or ind_line == -1:
                    pass
                else:
                    list_of_neighbors.append(matrix[ind_str - 1][ind_line])
            except:
                pass
            try:
                if ind_str - 1 == -1 or ind_line + 1 == -1:
                    pass
                else:
                    list_of_neighbors.append(matrix[ind_str - 1][ind_line + 1])
            except:
                pass
            try:
                if ind_str == -1 or ind_line - 1 == -1:
                    pass
                else:
                    list_of_neighbors.append(matrix[ind_str][ind_line - 1])
            except:
                pass
            try:
                if ind_str == -1 or ind_line + 1 == -1:
                    pass
                else:
                    list_of_neighbors.append(matrix[ind_str][ind_line + 1])
            except:
                pass
            try:
                if ind_str + 1 == -1 or ind_line - 1 == -1:
                    pass
                else:
                    list_of_neighbors.append(matrix[ind_str + 1][ind_line - 1])
            except:
                pass
            try:
                if ind_str + 1 == -1 or ind_line == -1:
                    pass
                else:
                    list_of_neighbors.append(matrix[ind_str + 1][ind_line])
            except:
                pass
            try:
                if ind_str + 1 == -1 or ind_line + 1 == -1:
                    pass
                else:
                    list_of_neighbors.append(matrix[ind_str + 1][ind_line + 1])
            except:
                pass

yes_or_not = 1 in list_of_neighbors
if yes_or_not == False:
    print("ДА")
else:
    print("НЕТ")