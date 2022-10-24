class Translator:
    DICT = {}

    def add(self, eng, rus):
        self.eng = eng
        self.rus = rus
        if self.eng in self.DICT and self.rus not in self.DICT[self.eng]:
            self.DICT[self.eng].append(self.rus)
        if self.eng not in self.DICT:
            self.DICT[self.eng] = [self.rus]

    def remove(self, eng):
        self.eng = eng
        self.DICT.pop(self.eng)

    def translate(self, eng):
        self.eng = eng
        print(*self.DICT[self.eng])


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
tr.translate("go")
tr.translate("tree")[0]
