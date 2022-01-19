import requests
import telebot
from telebot import types

TOKEN_openweathermap = 'e90957fbf95d9bcccb813873bc49c13c'
TOKEN = "2104027065:AAGlDLPCPWs9XNEhtKENexp7Dj_sTAA0RBk"
mybot = telebot.TeleBot(TOKEN)
lists = {}


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
    global lists
    if message.location is not None:
        longitud = message.location.longitude;
        latitud = message.location.latitude
        response = requests.get(
    'http://api.openweathermap.org/data/2.5/weather?lat=' + str(latitud) + '&lon=' + str(
        longitud) + '&lang=ru&units=metric&appid=' + TOKEN_openweathermap)
        lists = response.json()
        print(lists)
    weather(message)

def description():  # Дождь, туман и тд.
    a = lists['weather']
    b = (a[0])
    des = b['description']
    return (des)


def temp():  # Температура.
    tm = lists['main']['temp']
    return (tm)


def wind():  # Скорость вветра.
    sp = lists['wind']['speed']
    return (sp)


def location():  # Локация.
    loc = lists['name']
    return (loc)



def weather(message):
    mybot.send_message(message.chat.id, "Вы тут:  " + location() + "." + "\n" + "Температура: " + str(
        (temp())) + " С." + "\n" + "Ветер: " + str((wind())) + " м/с." + "\n" + description())


mybot.polling()

