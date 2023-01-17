class Clock:
    def __init__(self):
        __time = 0


    def set_time(self,tm):
        if __check_time(tm):
            self.__time = tm

    def  get_time(self):
        return self.__time


    def __check_time(self,tm):
        if tm in int and  0 <= tm < 100000:
            return True
