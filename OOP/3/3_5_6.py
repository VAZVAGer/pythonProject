text = "Мы будем устанавливать связь завтра днем"


class Morph:
    def __init__(self, *args):
        self.dictionary = list(map(lambda x: x.strip(" .,!?:;").lower(), args))

    def add_word(self, word):
        w = word.lower()
        if w not in self.dictionary:
            self.dictionary.append(w)

    def get_words(self):
        return tuple(self.dictionary)

    def __eq__(self, other):
        if type(other) != str:
            raise ValueError("оперант должен быть строкой")
        return other.lower() in self.dictionary


dict_words = [Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'),
              Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                    'формулах'),
              Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                    'векторами', 'векторах'),
              Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                    'эффектами', 'эффектах'),
              Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')]

words = map(lambda x: x.strip("?!;:,. ").lower(), text.split())
rec = sum(word == morph for word in words for morph in dict_words)
print(rec)