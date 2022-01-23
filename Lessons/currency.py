import requests
while True:
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    ExchangeRates = requests.get(url)
    lists = ExchangeRates.json()
    for dicts in lists:
        currency_code = dicts['r030']  # Код валюты
        currency_name = dicts['txt']  # Имя валюты
        print(currency_name + "-", currency_code)
    amount_of_money = float(input("Введите код валюты:"))
    for dicts2 in lists:
        currency_code = dicts2['r030']  # Код валюты
        currency_name = dicts2['txt']  # Имя валюты
        if currency_code == amount_of_money:
            print("Вы выбрали валюту:", currency_name)
            exchangeRates = dicts2['rate']  # курс
            amount_of_money = float(input("Введите кол-во валюты:"))
    try:
        uan = amount_of_money * exchangeRates   # Если код верен выполняется пересчет по курсу
        print('В гривнах:', uan)
    except:
        print("НЕСУЩЕСТВУЮЩИЙ КОД ВАЛЮТЫ!!!")   #Если код валюты несуществует, сообщает что код неверный
    input("Для продолжения нажмите 'ENTER'")