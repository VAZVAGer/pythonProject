from string import ascii_lowercase, digits
import re


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @classmethod
    def check_card_number(cls, number):
        pattern = r"\d\d\d\d-\d\d\d\d-\d\d\d\d-\d\d\d\d"
        match = re.fullmatch(pattern, number)
        return True if match else False

    @classmethod
    def check_name(cls, name):
        pattern = r'^[A-Z]{1,100}\s[A-Z]{1,100}$'
        match = re.fullmatch(pattern, name)
        return True if match else False