from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

def check_card_number(number):
    if type(number) in int:

        return True
    else:
        return False