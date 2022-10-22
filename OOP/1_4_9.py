import sys

# программу не менять, только добавить два метода
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200'] #list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока



class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):     # возвращает список из элементов списка lst_data в диапазоне [a; b] (включительно) по их индексам
                                # (не id, а индексам списка); также учесть, что граница b может превышать длину списка.
        return self.lst_data[a:b + 1]

    def insert(self, data):  #для добавления в список lst_data новых данных из переданного списка строк data;
        self.data_in = data
        for zn in self.data_in:
            zn.split(" ")



db = DataBase()
db.insert(lst_in)
