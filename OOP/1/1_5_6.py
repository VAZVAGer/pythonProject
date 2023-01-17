class Graph:
    def __init__(self, data):
        self.data = data
        self.is_show = True

    def set_data(self, data):
        self.data = data[:]

    def show_table(self):
        if self.is_show == False:
            print("Отображение данных закрыто")
        else:
            print(*self.data)

    def show_graph(self):
        if self.is_show == False:
            print("Отображение данных закрыто")
        else:
            print('Графическое отображение данных: ' + (" ".join(map(str, self.data))))

    def show_bar(self):
        if self.is_show == False:
            print("Отображение данных закрыто")
        else:
            print('Столбчатая диаграмма: ' + (" ".join(map(str, self.data))))
    def set_show(self, fl_show):
        self.is_show = fl_show


data_graph = [8, 11, 10, -32, 0, 7, 18]
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()