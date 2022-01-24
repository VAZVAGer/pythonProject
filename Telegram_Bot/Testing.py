from Api_coutrice import api_c
list_city = []
list = api_c['items']
for city_information in list:
    list_city.append(city_information['name'])
    list_city.sort() #Сортируем по алфавиту для удобства
print(list_city)