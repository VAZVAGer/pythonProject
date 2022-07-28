cities = ['Москва', 'Астрахань', 'Новгород', 'Димитровград', 'Душанбе']
initial = []
final_letter = [111]
for citie in cities:
    initial.append(citie[0].lower())

    if citie[-1].lower() == 'ь' or citie[-1].lower() == 'ъ' or citie[-1].lower() == 'ы':
        final_letter.append(citie[-2].lower())
    else:
        final_letter.append(citie[-1].lower())
final_letter.pop()
if initial[1::] == final_letter[1::]:
    print('ДА')
else:
    print("НЕТ")