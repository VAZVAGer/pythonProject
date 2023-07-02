
res = [[1, 2, 3, 4],    # [[6, 8],
       [5, 6, 7, 8],     # [9, 7]]
       [9, 8, 7, 6],
       [5, 4, 3, 2]]
class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix, *args, **kwargs):
