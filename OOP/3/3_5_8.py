class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls):
        return

    @classmethod
    def register(cls, money):
        money.cb = CentralBank


class Money:
    type_m = None

    def __init__(self, vol=0):
        self.__volume = vol
        self.__cb = None

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, zn):
        self.__volume = zn

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, zn):
        self.__cb = zn

    # def get_v(self, other):
    #     if self.cb is None:
    #         raise ValueError("Неизвестен курс валют.")
    #     if self.type_m is None:
    #         raise ValueError('Неизвестен тип кошелька')
    #     v1 = self.volume / self.cb.rates[self.type_m]
    #     v2 = other.volume / other.cb.rates[other.type_m]
    #     return v1 , v2
    def __eq__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if self.type_m is None:
            raise ValueError('Неизвестен тип кошелька')
        return abs(self.volume / self.cb.rates[self.type_m] - other.volume / other.cb.rates[other.type_m]) < 0.1
    def __lt__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if self.type_m is None:
            raise ValueError('Неизвестен тип кошелька')
        return self.volume / self.cb.rates[self.type_m] < other.volume / other.cb.rates[other.type_m]

    def __le__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if self.type_m is None:
            raise ValueError('Неизвестен тип кошелька')
        return self.volume / self.cb.rates[self.type_m] <= other.volume / other.cb.rates[other.type_m]

class MoneyR(Money):
    type_m = "rub"
class MoneyD(Money):
    type_m = "dollar"
class MoneyE(Money):
    type_m = "euro"


r = MoneyR(500)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r < d:
    print("неплохо")
else:
    print("нужно поднажать")