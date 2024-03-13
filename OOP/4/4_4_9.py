def class_log(log):
    def log_m(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, log_m_d(v))

        return cls
    def log_m_d(funk):
        def wrapper(*args, **kwargs):
            log.append(funk.__name__)
            return funk(*args, **kwargs)
        return wrapper
    return log_m

# здесь объявляйте декоратор и все что с ним связано

vector_log = []   # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value