# n, m = map(int, input().split())
# cities = list(map(str, input().split()))
cities = ['Москва', 'Астрахань', 'Новгород', 'Димитровград', 'Душанбе']
initial = [111]
final_letter = []
for citie in cities:
    initial.append(citie[0].lower())

    if citie[-1].lower() == 'ь' or citie[-1].lower() == 'ъ' or citie[-1].lower() == 'ы':
        final_letter.append(citie[-2].lower())
    else:
        final_letter.append(citie[-1].lower())


print(initial)
print(final_letter)
