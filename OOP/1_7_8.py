from string import ascii_lowercase, digits
import re

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    def check_card_number(number):
        if type(number) in int:
            if number == r'\d{4}-\d{4}-\d{4}-\d{4}' r'[A-Z]+\s[A-Z]+':
                return True
        else:
            return False

    def check_name(name):
#f'[{cls.CHARS_FOR_NAME}]+\s[{cls.CHARS_FOR_NAME}]+'