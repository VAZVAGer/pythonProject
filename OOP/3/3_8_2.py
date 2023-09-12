class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.__le = len(kwargs)
        self.__key = tuple(self.__dict__.keys())  #Формирует кортеж ключей

    def cheak_val(self, ind):
        if type(ind) != int or not (-self.__le <= ind < self.__le):
            raise IndexError('неверный индекс поля')

    def __getitem__(self, item):
        self.cheak_val(item)
        return getattr(self, self.__key[item])

    def __setitem__(self, key, value):
        self.cheak_val(key)
        return setattr(self, self.__key[key], value)