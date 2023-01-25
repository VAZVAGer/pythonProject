import random


class EmailValidator:
    symbols = 'abcdefghijklmnopqrstuvwxyz0123456789_.@'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        random_value = random.randrange(10, 15)
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
                if len(list_valid) == len(email):
                    return True
            else:
                return False

    @staticmethod
    def __character_length(email):
        counter = 0
        for symbol in email:
            if symbol != "@":
                counter += 1
            else:
                break
        if counter <= 99:
            return True
        else:
            return False

    @staticmethod
    def __length_after_character(email):
        counter = 0
        for symbol in email[::-1]:
            if symbol != "@":
                counter += 1
            else:
                break
        if counter <= 49:
            return True
        else:
            return False

    @staticmethod
    def __point_search(email):
        for symbol in email[::-1]:
            if symbol != "@":
                if symbol == ".":
                    return True
            else:
                break

    @staticmethod
    def __must_not_be(email):
        if ".." in email:
            return False
        else:
            return True

    @classmethod
    def check_email(cls, email):
        if EmailValidator.__is_email_str(email) and EmailValidator.__valid_symbols(
                email) and EmailValidator.__character_length(email) and EmailValidator.__length_after_character(
            email) and EmailValidator.__point_search(email) and EmailValidator.__must_not_be(email):
            return True
        else:
            return False


assert EmailValidator.check_email("sc_lib@list.ru") == True and EmailValidator.check_email(
    "sc_lib@list_ru") == False and EmailValidator.check_email("sc@lib@list_ru") == False and EmailValidator.check_email(
    "sc.lib@list_ru") == False and EmailValidator.check_email("sclib@list.ru") == True and EmailValidator.check_email(
    "sc.lib@listru") == False and EmailValidator.check_email(
    "sc..lib@list.ru") == False, "метод check_email отработал некорректно"

m = EmailValidator.get_random_email()
print(m)
assert EmailValidator.check_email(
    m) == True, "метод check_email забраковал сгенерированный email методом get_random_email"

assert EmailValidator() is None, "при создании объекта класса EmailValidator возвратилось значение отличное от None"

assert EmailValidator._EmailValidator__is_email_str('abc'), "метод __is_email_str() вернул False для строки"
