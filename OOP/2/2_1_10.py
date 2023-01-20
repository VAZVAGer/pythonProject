from string import ascii_lowercase, digits
import re
class EmailValidator:
    CHARS_FOR_NAME = ascii_lowercase.upper() + ascii_lowercase.lower() + digits + "_" + "."
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        pass

    def __is_email_str(cls, email):
        if type(email) == str:
            return True
        else:
            return False