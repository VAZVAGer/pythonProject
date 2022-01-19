import telebot
import requests
from telebot import types

TOKEN_openweathermap = 'e90957fbf95d9bcccb813873bc49c13c'
url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
ExchangeRates = requests.get(url)
lists = ExchangeRates.json()
TOKEN = "2104027065:AAGlDLPCPWs9XNEhtKENexp7Dj_sTAA0RBk"
mybot = telebot.TeleBot(TOKEN)
cpicok = []
codes = 0
amount_of_money = 0
uan = 0
lists2 = {}
for dicts in lists:
    currency_code = dicts['r030']  # Код валюты
    currency_name = dicts['txt']  # Имя валюты
    exchangeRates = dicts['rate']  # курс
    cpicok.append(currency_name + "-" + str(currency_code))
myString = "\n".join(cpicok)


@mybot.message_handler(commands=['start'])
def start(message):
    mybot.send_message(message.chat.id,
                       'Чтобы перевести валюту в гривну введите :/перевод\nДля того чтобы узнать погоду в месте вашего нахождения введите: /погода')


@mybot.message_handler(commands=['перевод'])  # Привводе команды старт , выводится список валют и кодов
def cur(message):
    mybot.send_message(message.chat.id, 'Выберете и введите код валюты :')
    mybot.send_message(message.chat.id, myString)
    mybot.send_message(message.chat.id, 'Выберете и введите код валюты :')
    mybot.register_next_step_handler(message, code)


def code(message):
    global codes;

    try:
        codes = int(message.text)  # проверяем, что од введен корректно
    except Exception:
        mybot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    mybot.send_message(message.from_user.id, 'ВЫ ВВЕЛИ ' + str(codes))
    mybot.send_message(message.from_user.id, 'Введите кол-во валюты: ')
    mybot.register_next_step_handler(message, amount)


def amount(message):
    global amount_of_money;

    try:
        amount_of_money = int(message.text)  # проверяем, что сод введен корректно
    except Exception:
        mybot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    mybot.send_message(message.from_user.id, 'ВЫ ВВЕЛИ ' + str(amount_of_money))
    currency(message)


def currency(message):
    global codes;
    for dicts2 in lists:
        currency_code = dicts2['r030']  # Код валюты
        currency_name = dicts2['txt']  # Имя валюты
        if currency_code == codes:
            exchangeRates = dicts2['rate']  # курс
    try:
        uan = amount_of_money * exchangeRates  # Если код верен выполняется пересчет по курсу
        mybot.send_message(message.from_user.id, str(uan) + "грн!")

    except:
        mybot.send_message(message.from_user.id,
                           "Веден не существующий код валюты")  # Если код валюты несуществует, сообщает что код неверный


@mybot.message_handler(commands=["погода"])
def start(message):
    # Клавиатура с кнопкой запроса локации
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    mybot.send_message(message.chat.id, "Поделись местоположением", reply_markup=keyboard)


# Получаю локацию
@mybot.message_handler(content_types=['location'])
def location(message):
    global lists2
    if message.location is not None:
        longitud = message.location.longitude;
        latitud = message.location.latitude
        response = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?lat=' + str(latitud) + '&lon=' + str(
                longitud) + '&lang=ru&units=metric&appid=' + TOKEN_openweathermap)
        lists2 = response.json()
        print(lists2)
    weather(message)


def description():  # Дождь, туман и тд.
    a = lists2['weather']
    b = (a[0])
    des = b['description']
    return (des)


def temp():  # Температура.
    tm = lists2['main']['temp']
    return (tm)


def wind():  # Скорость вветра.
    sp = lists2['wind']['speed']
    return (sp)


def locat():  # Локация.
    loc = lists2['name']
    return (loc)


def weather(message):
    mybot.send_message(message.chat.id, "Вы тут:  " + locat() + "." + "\n" + "Температура: " + str(
        (temp())) + " С." + "\n" + "Ветер: " + str((wind())) + " м/с." + "\n" + description())


mybot.polling()
