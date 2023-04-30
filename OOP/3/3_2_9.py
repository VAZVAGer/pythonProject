class InputDigits:
    def __init__(self, funk):
        self.funk = funk

    def __call__(self, *args, **kwargs):
        sp = self.funk().split()
        ls = list(map(int, sp))
        return ls


input_dg = InputDigits(input)
res = input_dg()
