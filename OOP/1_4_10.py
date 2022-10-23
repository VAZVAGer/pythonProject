class Translator:
    DICT = {}
    def add(self, eng, rus):
        self.eng = eng
        self.rus = rus
        if self.eng in self.DICT:
            self.DICT["go"].append(self.rus)

        else:
            self.DICT[self.eng] = [self.rus]
        print(self.DICT)


ob_1 = Translator()
ob_1.add("go", "идти")
ob_1.add("go", "бег")
ob_1.add("name", "имя")
ob_1.add("go", "идти")
