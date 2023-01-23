
import re
import random
class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        random_value = random.randrange(1, 100)
        random_mail = random.sample('abcdefghijklmnopqrstuvwxyz0123456789_.', random_value)
        random_mail = ''.join(random_mail)
        random_mail = random_mail + "@gmail.com"
        return random_mail

    def __is_email_str(cls, email):
        if type(email) == str:
            return True
        else:
            return False
    def check_email(cls, email):
        if EmailValidator.__is_email_str():
            pass
        else:
            return False


