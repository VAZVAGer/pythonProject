class Money:
    def __init__(self, money=0):
        self.__money = money

    def __check_money(self, money):
        if self.__money == type(int) and self.__money >= 0:
            return True
    def set_money(self, money):
        if self.__check_money():
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(mn):