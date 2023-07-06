# res = [[1, 2, 3, 4],  # [[6, 8],
#        [5, 6, 7, 8],  # [9, 7]]
#        [9, 8, 7, 6],
#        [5, 4, 3, 2]]


class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size
    def Max_Pooling(self, matrix):
        caunter = 0
        step_r = 0
        rezalt = []
        caunter_sector = 0
        caunter_sector_2 = 0
        while caunter != len(matrix) and step_r < len(matrix):
            sector = []
            try:
                for indX in range(caunter, caunter + self.size[-1]):  # строки перебирает
                    sector += matrix[indX][step_r:self.size[0] + step_r]
            except:
                break
            caunter += self.step[0]
            if caunter_sector < len(matrix):
                rezalt.append([max(sector)])
                caunter_sector += self.step[0]
            if caunter == len(matrix):
                caunter = 0
                step_r += self.step[-1]
                rezalt[caunter_sector_2].append(max(sector))
                caunter_sector_2 += 1
        return rezalt
    def __call__(self, matrix, *args, **kwargs):
        for indx in range(len(matrix)-1):
            if len(matrix[indx]) != len(matrix[indx + 1]):
                raise ValueError("Неверный формат для первого параметра matrix.")
        for i in matrix:
            for ii in i:
                if type(ii) != int and type(ii) != float:
                    raise ValueError("Неверный формат для первого параметра matrix.")

        return MaxPooling.Max_Pooling(self, matrix)



mp = MaxPooling(step=(2, 2), size=(2,2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12],
      [5, 10, 0, -5],
      [0, 1, 2, 300],
      [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)

assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2, 2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"