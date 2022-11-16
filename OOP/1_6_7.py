class SingletonFive:
    __ss = None
    c = 0
    def __new__(cls, *args, **kwargs):

        if cls.c != 5:
            cls.c += 1
            cls.__ss = super().__new__(cls)
        return cls.__ss


    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
print(*objs, sep='\n')