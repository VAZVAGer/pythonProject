class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.count = -1
        self.list_atr = [self.fio, self.job, self.old, self.salary, self.year_job]

    def __getitem__(self, item):
        if type(item) == int and 0 <= item <= len(self.list_atr) - 1:
            return self.list_atr[item]
        else:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        if type(key) == int and 0 <= key <= len(self.list_atr) - 1:
            self.list_atr[key] = value
        else:
            raise IndexError('неверный индекс')


    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count < len(self.list_atr):
            return self.list_atr[self.count]
        raise StopIteration



pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123