import sys

# программу не менять, только добавить два метода
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200'] #list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока



class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):  #для добавления в список lst_data новых данных из переданного списка строк data;
        self.data_in = data
        for velue in self.data_in:
            data = velue.split(" ")
            dic = {}
            for index, velue2 in enumerate(data):
                dic[self.FIELDS[index]] = velue2
            self.lst_data.append(dic)
    def select(self, a, b):
        self.a = a
        self.b = b
        return self.lst_data[a:b + 1]



db = DataBase()
db.insert(lst_in)
