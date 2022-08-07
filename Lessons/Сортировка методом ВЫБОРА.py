matrix = [8, 11, -53, 2, 10, 12]
ind = len(matrix)
for index_1 in range(ind - 1):
    znachenie_1 = matrix[index_1]
    MINI = matrix[index_1]
    MINI_id = index_1
    for index_2 in range(index_1, ind):
        znachenie_2 = matrix[index_2]
        if znachenie_2 < MINI:
            MINI = znachenie_2
            MINI_id = index_2
    matrix[index_1], matrix[MINI_id] = matrix[MINI_id], matrix[index_1]

print(*matrix)