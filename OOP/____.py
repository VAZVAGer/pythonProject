res = [[1, 10, 10, 12],
      [5, 10, 0, -5],
      [0, 1, 2, 300],
      [40, -100, 0, 54.5]]
size = (2, 2)
step = (2, 2)


def Max_Pooling(matrix):
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

    print(rezalt)


Max_Pooling(res)
