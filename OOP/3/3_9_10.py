class Matrix:
    def cheack_list2D(self, list):
        len_line = len(list[0])
        for line in list:
            if len(line) != len_line:
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            for element in line:
                if type(element) != int and type(element) != float:
                    raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    def __init__(self, *args):
        if len(args) == 3:
            if type(args[0]) != int or type(args[1]) != int and isinstance(args[2], (int, float)):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.__rows = args[0]
            self.__cols = args[1]
            self.__matriX = list(list(args[2] for _ in range(self.__cols)) for _ in range(self.__rows))
        elif len(args) == 1:
            self.cheack_list2D(args[0])
            self.__matriX = args[0]

    def __len__(self):
        return len(self.__matriX)

    def __getitem__(self, item):
        if type(item) == int:
            return self.__matriX[item]
        ind1, ind2 = item
        if (not isinstance(ind1, int) or not isinstance(ind2, int) or not (0 <= ind1 <= len(self.__matriX) - 1) or
        not (0 <= ind2 <= len(self.__matriX[ind1]) - 1)):
            raise IndexError('недопустимые значения индексов')
        return self.__matriX[ind1][ind2]

    def __setitem__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')
        ind1, ind2 = key
        self.__matriX[ind1][ind2] = value

    def __eq__(self, other):
        return len(self) == len(other)

    def __add__(self, other):
        new_matrix = []
        if type(other) == Matrix:
            if self != other:
                raise ValueError('операции возможны только с матрицами равных размеров')
            for ind_1, line in enumerate(self):
                new_line_matrix = []
                for ind_2, value in enumerate(line):
                    new_value = self[ind_1][ind_2] + other[ind_1][ind_2]
                    new_line_matrix.append(new_value)
                new_matrix.append(new_line_matrix)
            return Matrix(new_matrix)
        elif isinstance(other, (int, float)):
            for ind_1, line in enumerate(self):
                new_line_matrix = []
                for ind_2, value in enumerate(line):
                    new_value = self[ind_1][ind_2] + other
                    new_line_matrix.append(new_value)
                new_matrix.append(new_line_matrix)
            return Matrix(new_matrix)

    def __sub__(self, other):
        new_matrix = []
        if type(other) == Matrix:
            if self != other:
                raise ValueError('операции возможны только с матрицами равных размеров')
            for ind_1, line in enumerate(self):
                new_line_matrix = []
                for ind_2, value in enumerate(line):
                    new_value = self[ind_1][ind_2] - other[ind_1][ind_2]
                    new_line_matrix.append(new_value)
                new_matrix.append(new_line_matrix)
            return Matrix(new_matrix)
        elif isinstance(other, (int, float)):
            for ind_1, line in enumerate(self):
                new_line_matrix = []
                for ind_2, value in enumerate(line):
                    new_value = self[ind_1][ind_2] - other
                    new_line_matrix.append(new_value)
                new_matrix.append(new_line_matrix)
            return Matrix(new_matrix)


list2D = [[1, 2], [3, 4], [5, 6, 7]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

list2D = [[1, []], [3, 4], [5, 6]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

try:
    st = Matrix('1', 2, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

list2D = [[1, 2], [3, 4], [5, 6]]
matrix = Matrix(list2D)
assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

matrix = Matrix(4, 5, 10)
assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

try:
    v = matrix[3, -1]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

try:
    v = matrix['0', 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

matrix[0, 0] = 7
assert matrix[0, 0] == 7, "неверно отработал __setitem__"

try:
    matrix[0, 0] = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError в __setitem__"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1], [1, 1]])

try:
    matrix = m1 + m2
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1]])
matrix = m1 + m2
assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
       and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
m = matrix + 10
assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
       and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"
