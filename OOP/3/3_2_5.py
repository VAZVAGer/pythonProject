class DigitRetrieve:

    def __call__(self, namder, *args, **kwargs):
        try:
            namder = int(namder)
            return namder
        except:
            return None
dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)