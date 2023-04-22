import time


class Mechanical:
    def __init__(self, date=0):
        self.date = date

    def __setattr__(self, key, value):
        if self.__dict__.get("date"):
            return None
        return object.__setattr__(self, key, value)


class Aragon:
    def __init__(self, date=0):
        self.date = date

    def __setattr__(self, key, value):
        if self.__dict__.get("date"):
            return None
        return object.__setattr__(self, key, value)


class Calcium:
    def __init__(self, date=0):
        self.date = date

    def __setattr__(self, key, value):
        if self.__dict__.get("date"):
            return None
        return object.__setattr__(self, key, value)


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slot_list = [None, None, None]

    def add_filter(self, slot_num, filter):
        if type(filter) == Mechanical and slot_num == 1 and self.slot_list[0] == None:
            self.slot_list[0] = filter

        elif type(filter) == Aragon and slot_num == 2 and self.slot_list[1] == None:
            self.slot_list[1] = filter

        elif type(filter) == Calcium and slot_num == 3 and self.slot_list[2] == None:
            self.slot_list[2] = filter

    def remove_filter(self, slot_num):
        if self.slot_list[slot_num - 1] != None:
            self.slot_list[slot_num - 1] = None

    def get_filters(self):
        return tuple(self.slot_list)

    def water_on(self):
        if None not in self.slot_list:
            if 0 <= (time.time() - self.slot_list[0].date) <= self.MAX_DATE_FILTER and 0 <= (
                    time.time() - self.slot_list[1].date) <= self.MAX_DATE_FILTER and 0 <= (
                    time.time() - self.slot_list[2].date) <= self.MAX_DATE_FILTER:
                return True
            else:
                return False
        if None in self.slot_list:
            return False


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))

assert my_water.water_on() == False, "метод water_on вернул True, хотя не все фильтры были установлены"

my_water.add_filter(3, Calcium(time.time()))
assert my_water.water_on(), "метод water_on вернул False при всех трех установленных фильтрах"

f1, f2, f3 = my_water.get_filters()
assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(f3,
                                                                            Calcium), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"

my_water.remove_filter(1)
assert my_water.water_on() == False, "метод water_on вернул True, хотя один из фильтров был удален"

my_water.add_filter(1, Mechanical(time.time()))
assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"

f1, f2, f3 = my_water.get_filters()
my_water.remove_filter(1)

my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
assert my_water.water_on() == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"

f1 = Mechanical(1.0)
f2 = Aragon(2.0)
f3 = Calcium(3.0)
assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"

f1.date = 5.0
f2.date = 5.0
f3.date = 5.0

assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"
