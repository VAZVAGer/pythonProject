res = [[1, 2, 3, 4],  # [[6, 8],
       [5, 6, 7, 8],  # [9, 7]]
       [9, 8, 7, 6],
       [5, 4, 3, 2]]
size = (2, 2)
step = (2, 2)


# print(max(res[0][0:2]+res[1][0:2]))

def MaxPooling(matrix):
    caunt = 0

    while caunt != len(matrix):
        sector = []
        for indX in range(caunt, caunt + size[1]):  # строки перебирает
            sector += matrix[indX][0:size[0]]
        caunt += step[0]

        print(sector)


MaxPooling(res)
