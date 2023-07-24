stich = ["Я к вам пишу –чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]


class StringText:
    def __init__(self, lst_words):
        self.lsttext = lst_words

    def __lt__(self, other):
        return len(self.lsttext) < len(other.lsttext)

    def __le__(self, other):
        return len(self.lsttext) <= len(other.lsttext)
lst_text = []
def rrr(arg):

    for line in stich:
        Lst_line = line.split()
        line = []
        for word in Lst_line:
            ll = word.strip("–?!,.;")
            line.append(ll)
        lst_text.append(StringText(line))

    return lst_text

def extractor(data_list):
    lst_text_sorted = []
    for class_instance in data_list:
        lst_text_sorted.append(class_instance.lsttext)

    lst_text_sorted2 = []
    for stroca in lst_text_sorted:
        lst_text_sorted2.append(' '.join(stroca))
    return lst_text_sorted2

lst_text_sorted = sorted(rrr(stich), reverse=True)

extractor(lst_text_sorted)
print(extractor(lst_text_sorted))

assert all([[True if i in _ else False for i in "–?!,.;"] for _ in stich]), \
    "в stich есть знаки которые нужно удалить - (–?!,.;)"
assert len(lst_text) == 7 and all(
    True if isinstance(_, StringText) else False for _ in lst_text), "ошибка в lst_text"

assert lst_text_sorted == ['Я к вам пишу чего же боле',
                           'Теперь я знаю в вашей воле',
                           'Но вы к моей несчастной доле',
                           'Что я могу еще сказать',
                           'Хоть каплю жалости храня',
                           'Вы не оставите меня',
                           'Меня презреньем наказать'], "неверно отсортирован список lst_text_sorted"

assert lst_text[0] > lst_text[4] and lst_text[4] > lst_text[1], "метод > работает неверно"
assert lst_text[1] < lst_text[4], "метод < работает неверно"

assert lst_text[2] >= lst_text[4], "метод >= работает неверно"
assert lst_text[2] <= lst_text[4], "метод >= работает неверно"

print("Правильный ответ.")