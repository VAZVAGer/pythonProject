class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls):
        return

    @classmethod
    def register(cls, money):
        money.cb = CentralBank


class MoneyR:
    currency = 'rub'

    def __init__(self, vol=0):
        self.volum = vol
        self.cb = None

    @property
    def volum(self):
        return self.__volum

    @volum.setter
    def volum(self, zn):
        if type(zn) == int or type(zn) == float:
            self.__volum = zn

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, zn):
        self.__cb = zn

    def __lt__(self, other):
        return self.volum / self.cb.rates[self.currency] < other.volum / other.cb.rates[self.currency]

    def __eq__(self, other):
        return self.volum / self.cb.rates[self.currency] == other.volum / other.cb.rates[self.currency]

    def __le__(self, other):
        return self.volum / self.cb.rates[self.currency] <= other.volum / other.cb.rates[self.currency]


class MoneyD:
    currency = 'dollar'

    def __init__(self, vol=0):
        self.volum = vol
        self.cb = None

    @property
    def volum(self):
        return self.__volum

    @volum.setter
    def volum(self, zn):
        if type(zn) == int or type(zn) == float:
            self.__volum = zn

    @property
    def cb(self):
        return self.__cd

    @cb.setter
    def cb(self, zn):
        self.__cb = zn

    def __lt__(self, other):
        return self.volum / self.cb.rates[self.currency] < other.volum / other.cb.rates[self.currency]

    def __eq__(self, other):
        return self.volum / self.cb.rates[self.currency] == other.volum / other.cb.rates[self.currency]

    def __le__(self, other):
        return self.volum / self.cb.rates[self.currency] <= other.volum / other.cb.rates[self.currency]


class MoneyE:
    currency = 'euro'

    def __init__(self, vol=0):
        self.volum = vol
        self.cb = None

    @property
    def volum(self):
        return self.__volum

    @volum.setter
    def volum(self, zn):
        if type(zn) == int or type(zn) == float:
            self.__volum = zn

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, zn):
        self.__cb = zn

    def __lt__(self, other):
        return self.volum / self.cb.rates[self.currency] < other.volum / other.cb.rates[self.currency]

    def __eq__(self, other):
        return self.volum / self.cb.rates[self.currency] == other.volum / other.cb.rates[self.currency]

    def __le__(self, other):
        return self.volum / self.cb.rates[self.currency] <= other.volum / other.cb.rates[self.currency]
