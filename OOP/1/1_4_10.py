class Translator:
    def add(self, eng, rus):
        if "DICT" not in self.__dict__:
            self.DICT = {}
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
        return self.DICT[self.eng]


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
print(*tr.translate("go"))

