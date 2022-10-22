lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
FIELDS = ('id', 'name', 'old', 'salary')
for velue in lst_in:
    data = velue.split(" ")
    dic = {}
    for index, velue2 in enumerate(data):
        dic[FIELDS[index]] = velue2
    print(dic)

