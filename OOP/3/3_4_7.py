class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, vel):
        if type(vel) is str:
            self.__title = vel

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, vel):
        if type(vel) is str:
            self.__author = vel

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, vel):
        if type(vel) is int:
            self.__year = vel


class Lib:
    def __init__(self):
        self.book_list = []

    def __len__(self):
        return len(self.book_list)

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if type(other) == Book:
            for n, i in enumerate(self.book_list):
                if other.title == i.title and other.author == i.author and other.year == i.year:
                    self.book_list.pop(n)
            return self
        elif type(other) == int:
            self.book_list.pop(other)
            return self


lib = Lib()

lib = lib + Book('Процесс', 'Кафка', 2020)  # добавление новой книги в библиотеку

lib += Book('Три товарища', 'Ремарк', 2021)

lib += Book('Бесы', 'Достоевский', 2022)

lib += Book('1984', 'Оруэлл', 2022)

print(len(lib))

lib = lib - Book('Процесс', 'Кафка', 2020)  # удаление книги book из библиотеки

lib -= Book('Три товарища', 'Ремарк', 2021)

print(len(lib))
lib = lib - 1  # удаление книги по ее порядковому номеру

lib -= 0

print(len(lib))
