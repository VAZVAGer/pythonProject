class Vector:
    def __init__(self, *args):
        self.cord_vector = args

    def dimensional_check(self, other):
        if len(self.cord_vector) != len(other.cord_vector):
            raise ArithmeticError('размерности векторов не совпадают')
        return True

    def __add__(self, other):
        add_cord_vector = []
        self.dimensional_check(other)
        for ind, i1 in enumerate(self.cord_vector):
            add_cord_vector.append(other.cord_vector[ind] + i1)
        return Vector(tuple(add_cord_vector))

    def __sub__(self, other):
        sub_cord_vector = []
        self.dimensional_check(other)
        for ind, i1 in enumerate(self.cord_vector):
            sub_cord_vector.append(i1 - other.cord_vector[ind])
        return Vector(tuple(sub_cord_vector))

    def __mul__(self, other):
        mul_cord_vector = []
        self.dimensional_check(other)
        for ind, i1 in enumerate(self.cord_vector):
            mul_cord_vector.append(other.cord_vector[ind] * i1)
        return Vector(tuple(mul_cord_vector))

    def __iadd__(self, other):
        if type(other) == Vector:
            self.dimensional_check(other)
            for ind, i1 in enumerate(self.cord_vector):
                self.cord_vector[ind] == i1 + other.cord_vector[ind]

        elif type(other) == int:
            for ind, i1 in enumerate(self.cord_vector):
                self.cord_vector[ind] == i1 + other

        return self

    def __isub__(self, other):
        if type(other) == Vector:
            self.dimensional_check(other)
            for ind, i1 in enumerate(self.cord_vector):
                self.cord_vector[ind] == i1 - other.cord_vector[ind]

        elif type(other) == int:
            for ind, i1 in enumerate(self.cord_vector):
                self.cord_vector[ind] == i1 - other

        return self

    def __eq__(self, other):
        if len(self.cord_vector) != len(other.cord_vector):
            return False
        else:
            for ind, i1 in enumerate(self.cord_vector):
                if i1 == other.cord_vector[ind]:
                    return True
                else:
                    return False

    def __ne__(self, other):
        if len(self.cord_vector) != len(other.cord_vector):
            return True
        else:
            for ind, i1 in enumerate(self.cord_vector):
                if i1 != other.cord_vector[ind]:
                    return True
                else:
                    return False
