import requests
import telebot
from telebot import types
from Api_sity import api_s
from Api_coutrice import api_c

API_key_sity = "a9d781a8d9c03224b95a996b1abe23e9"
TOKENBOT = "2104027065:AAGlDLPCPWs9XNEhtKENexp7Dj_sTAA0RBk"
mybot = telebot.TeleBot(TOKENBOT)
url_countries = "http://htmlweb.ru/geo/api.php?location&json&api_key=API_key_sity" #Списог стран.
ExchangeRates = requests.get(url_countries)
lists = ExchangeRates.json()
print(lists)
List_of_countries = []
request_c = 0
match_by_country = []
list_c = []
for dicts in lists:
    try:
        countries = lists[dicts]['name']
        List_of_countries.append(countries)
    except:
        pass


@mybot.message_handler(commands=['start'])
def start(message):
    mybot.send_message(message.chat.id, 'Введите название страны, можно не полностью.')
    mybot.register_next_step_handler(message, country_request)
    mybot.register_next_step_handler(message, button)


def country_request(message):
    global request_c
    request_c = message.text  # Воовд названия страны которую ищу или части ее названия.
    countries()


def countries():
    global match_by_country
    for i in List_of_countries:
        if request_c in i:
            match_by_country.append(i)


def button(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for count_button in match_by_country:
        button_с = types.KeyboardButton(text=count_button)
        keyboard.add(button_с)
    mybot.send_message(message.chat.id, 'Вы ввели: ' + request_c, reply_markup=keyboard)
    mybot.register_next_step_handler(message, selected_country)


def selected_country(message):
    global list_c
    selected_country = message.text  # выбранная страна по нажатию кнопки из списка.
    print(selected_country)

    url_city = "http://htmlweb.ru/json/geo/city_list?country=" + selected_country + "&api_key=" + API_key_sity #Список городов выбраной страны
    ExchangeRates = requests.get(url_city)
    list_city = ExchangeRates.json()
    print(list_city)
    list2 = list_city['items']
    for city_information in list2:
        list_c.append(city_information['name'])
        list_c.sort()  # Сортируем по алфавиту для удобства
    print(list_c)





mybot.polling()
