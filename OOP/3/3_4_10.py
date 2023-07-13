# res = [[1, 2, 3, 4],  # [[6, 8],
#        [5, 6, 7, 8],  # [9, 7]]
#        [9, 8, 7, 6],
#        [5, 4, 3, 2]]


class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def Max_Pooling(self, matrix):
        matrix_pattern = []
        list_values = []
        for ind_step_right in range(0, len(matrix[0]), self.step[-1]):
            matrix_pattern.append([])
            for ind_step_down in range(0, len(matrix), self.step[0]):
                sector = []
                if len(matrix[ind_step_down][ind_step_right:ind_step_right + self.size[0]]) != self.size[0]:
                    matrix_pattern.pop()
                    break
                else:
                    sector.append(
                        max(matrix[ind_step_down][ind_step_right:ind_step_right + self.size[0]]))  # первая строчка чектора
                    for ind_size in range(ind_step_down + 1, self.size[-1] + ind_step_down):  # последующие строки сектора
                        if ind_size < len(matrix):
                            sector.append(max(matrix[ind_size][ind_step_right:ind_step_right + self.size[0]]))

                if len(sector) == self.size[-1]:
                    list_values.append(max(sector))



        counter = 0
        counter_2 = 0
        while counter_2 < len(list_values):
            counter += counter_2
            for ind, ls in enumerate(matrix_pattern):
                ls.append(list_values[counter_2])
                counter_2 += 1
        return matrix_pattern
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