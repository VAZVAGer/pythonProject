res = [[1, 2, 3, 4],  # [[6, 8],
       [5, 6, 7, 8],  # [9, 7]]
       [9, 8, 7, 6],
       [5, 4, 3, 2]]
size = (2, 2)
step = (2, 2)


def MaxPooling(matrix):
    caunter = 0
    step_r = 0
    rezalt = []
    caunter_sector = 0
    caunter_sector_2 = 0
    while caunter != len(matrix) and step_r < len(matrix):
        sector = []
        for indX in range(caunter, caunter + size[-1]):  # строки перебирает
            sector += matrix[indX][step_r:size[0] + step_r]
        caunter += step[0]
        if caunter_sector < len(matrix):
            rezalt.append([max(sector)])
            caunter_sector += step[0]
        if caunter == len(matrix):
            caunter = 0
            step_r += step[-1]
            rezalt[caunter_sector_2].append(max(sector))
            caunter_sector_2 += 1

    return rezalt


MaxPooling(res)
