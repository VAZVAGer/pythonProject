import re
import random


class EmailValidator:
    symbols = 'abcdefghijklmnopqrstuvwxyz0123456789_.@'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        random_value = random.randrange(1, 100)
        random_mail = random.sample(EmailValidator.symbols, random_value)
        random_mail = ''.join(random_mail)
        random_mail = random_mail + "@gmail.com"
        return random_mail

    @staticmethod
    def __is_email_str(email):
        if type(email) == str:
            return True
        else:
            return False

    @staticmethod
    def __valid_symbols(email):
        list_valid = []
        for symbol in email:
            if EmailValidator.symbols.find(symbol) != -1:
                list_valid.append(symbol)
            if len(list_valid) == email:
                return True
            else:
                return False



    @classmethod
    def check_email(cls, email):
        if EmailValidator.__is_email_str():

        else:
            return False
