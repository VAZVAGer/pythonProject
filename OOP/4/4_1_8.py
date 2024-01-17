class Validator:
    def _is_valid(self, data):
        if data != None:
            return True
    def __call__(self, data, *args, **kwargs):
        if self._is_valid(data):
            return data
        else:
            raise ValueError('данные не прошли валидацию')

class IntegerValidator(Validator): ## для проверки, что data - целое число в заданном диапазоне;
    def __init__(self, min_value, max_value):
        self.min = min_value
        self.max = max_value

    def _is_valid(self, data):
        if type(data) == int:
            if self.min <= data <= self.max:
                return True
        return False

class FloatValidator(Validator): ## для проверки, что data - вещественное число в заданном диапазоне.
    def __init__(self, min_value, max_value):
        self.min = min_value
        self.max = max_value

    def _is_valid(self, data):
        if type(data) == float:
            if self.min <= data <= self.max:
                return True
        return False


