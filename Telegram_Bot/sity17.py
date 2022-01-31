import requests
import telebot
from telebot import types
from Api_sity import api_s
from Api_coutrice import api_c

TOKEN_openweathermap = 'e90957fbf95d9bcccb813873bc49c13c'  # Ключ погоды
API_key_sity = "a9d781a8d9c03224b95a996b1abe23e9"  # Ключ стран и городов
TOKENBOT = "2104027065:AAGlDLPCPWs9XNEhtKENexp7Dj_sTAA0RBk"  # Ключ Телеграм бота
mybot = telebot.TeleBot(TOKENBOT)
url_countries = "http://htmlweb.ru/geo/api.php?location&json&api_key=API_key_sity"  # Список стран.
ExchangeRates = requests.get(url_countries)
lists = ExchangeRates.json()
print(lists)  # Вывод содержимого API стран.
List_of_countries = []
request_c = 0
match_by_country = []
list_c = []
weather_data = []
for dicts in lists:
    try:
        countries = lists[dicts]['name']
        List_of_countries.append(countries)
    except:
        pass


@mybot.message_handler(commands=['start'])  # Запускает бота.
def start(message):
    mybot.send_message(message.chat.id, 'Введите название страны, можно не полностью.')
    mybot.register_next_step_handler(message, country_request)
    mybot.register_next_step_handler(message, button_coutris)


def country_request(message):
    global request_c
    request_c = message.text.lower()  # Воовд названия страны которую ищу или части ее названия.
    global match_by_country
    for i in List_of_countries:
        if request_c in i.lower():
            match_by_country.append(i)
        else:
            mybot.send_message(message.chat.id, "Запрос введен не верно!\nHачните заново отправив '/start'" )
            return

def button_coutris(message):  # Получаем кнопки со странами.
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for count_button in match_by_country:
        button_с = types.KeyboardButton(text=count_button)
        keyboard.add(button_с)
    mybot.send_message(message.chat.id, 'Вы ввели: ' + request_c, reply_markup=keyboard)
    mybot.register_next_step_handler(message, selected_country)


def selected_country(message):
    global list_c
    selected_country = message.text  # выбранная страна по нажатию кнопки из списка.
    print(selected_country)  # Вывод выбранной страны.

    url_city = "http://htmlweb.ru/json/geo/city_list?country=" + selected_country + "&api_key=" + API_key_sity  # Список городов выбраной страны
    ExchangeRates = requests.get(url_city)
    list_city = ExchangeRates.json()
    print(list_city)  # Вывод API городов.
    list2 = list_city['items']
    for city_information in list2:
        list_c.append(city_information['name'])
        list_c.sort()  # Сортируем по алфавиту для удобства
    print(list_c)  # Вывод списка городов выбраной страны.
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for count_button2 in list_c:
        button_сit = types.KeyboardButton(text=count_button2)
        keyboard.add(button_сit)
    mybot.send_message(message.chat.id, 'Выберете город, что бы получить прогноз погоды:', reply_markup=keyboard)
    mybot.register_next_step_handler(message, selected_city)


def selected_city(message):
    global weather_data
    selected_country = message.text  # выбранный город по нажатию кнопки из списка.
    print(selected_country)
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=' + selected_country + '&units=metric&appid=' + TOKEN_openweathermap)
    weather_data = response.json()
    print(weather_data)
    weather(message)


def description():  # Дождь, туман и тд.
    a = weather_data['weather']
    b = (a[0])
    des = b['description']
    return (des)


def temp():  # Температура.
    tm = weather_data['main']['temp']
    return (tm)


def wind():  # Скорость вветра.
    sp = weather_data['wind']['speed']
    return (sp)


def location():  # Локация.
    loc = weather_data['name']
    return (loc)


def weather(message):
    mybot.send_message(message.chat.id, "Вы тут:  " + location() + "." + "\n" + "Температура: " + str(
        (temp())) + " С." + "\n" + "Ветер: " + str((wind())) + " м/с." + "\n" + description())


mybot.polling()
