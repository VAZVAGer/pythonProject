class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.column = column


    def __iter__(self):
        self.row = 0
        return self

    def __next__(self):
        if self.row < len(self.lst):
            value = self.lst[self.row][self.column]
            self.row += 1
            return value

        else:
            raise StopIteration


lst = [[1, 11, 111],
       [2, 22, 222, 2222, 22222, 222222],
       [3, 33, 333, 3333, 33333, 333333],
       [4, 44, 444, 4444, 44444, 444444]]
it = IterColumn(lst, 2)
for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)
it_iter = iter(it)
# x = next(it_iter)
#
# print(next(it_iter))
# print(next(it_iter))
# print(next(it_iter))
# print(next(it_iter))
#
