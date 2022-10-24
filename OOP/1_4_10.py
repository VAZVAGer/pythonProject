class Translator:
    DICT = {}
    def add(self, eng, rus):
        self.eng = eng
        self.rus = rus
        if self.eng in self.DICT and self.rus not in self.DICT[self.eng]:
            self.DICT[self.eng].append(self.rus)
        if self.eng not in self.DICT:
            self.DICT[self.eng] = [self.rus]



ob_1 = Translator()
ob_1.add("go", "идти")
ob_1.add("go", "бег")
ob_1.add("name", "имя")
ob_1.add("go", "идти")
