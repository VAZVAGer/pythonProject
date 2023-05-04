class WordString:
    def __init__(self):
        self.string = None

    def __len__(self):
        return len(self.string.split(" "))

    def __call__(self, *args, **kwargs):
        return self.string[args[0]]

    @property
    def string(self):
        return self.string

    @string.setter
    def string(self, string):
        self.string = string



words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")