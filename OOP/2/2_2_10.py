class PhoneBook:
    def __init__(self):
        self.book = []

    def add_phone(self, phone):
        self.book.append(phone)

    def remove_phone(self, indx):
        self.book.pop(indx)

    def get_phone_list(self):
        return self.book


class PhoneNumber:
    def __init__(self, number, fio):
        self.__number = number
        self.__fio = fio

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if type(number) == int and len(number) == 11:
            self.__number = number

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.__fio = fio
