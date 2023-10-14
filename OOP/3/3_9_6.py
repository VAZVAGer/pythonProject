class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst



    def __iter__(self):
        self.row = 0
        self.element = 0
        return self

    def __next__(self):
        if self.row == self.element:
            value = self.lst[self.row][self.element]
            self.row += 1
            self.element = 0
            return value
        elif self.row > self.element and self.row < len(self.lst):
            value1 = self.lst[self.row][self.element]
            self.element += 1
            return value1

        else:
            raise StopIteration








lst = [[1, 11, 111, 1111, 11111, 111111],
       [2, 22, 222, 2222, 22222, 222222],
       [3, 33, 333, 3333, 33333, 333333],
       [4, 44, 444, 4444, 44444, 444444]]
it = TriangleListIterator(lst)
for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)
