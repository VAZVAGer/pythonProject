lst_in = ['Python; Балакирев С.М.; 2020', 'Python ООП; Балакирев С.М.; 2021', 'Python ООП; Балакирев С.М.; 2022',
          'Python; Балакирев С.М.; 2021']


class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_bs = []

for l in lst_in:
    ll = l.split(";")
    lst_bs.append(BookStudy(ll[0], ll[1], int(ll[-1])))

ss = set(lst_bs)

unique_books = len(ss)

print(unique_books)
