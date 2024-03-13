class Aircraft:
    def ch(self, value):
        if value < 1:
            raise TypeError('неверный тип аргумента')

    def __init__(self, model, mass, speed, top):
        if type(model) != str:
            raise TypeError('неверный тип аргумента')
        self._model = model
        self.ch(mass)
        self._mass = mass
        self.ch(speed)
        self._speed = speed
        self.ch(top)
        self._top = top


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        if type(chairs) != int or chairs < 0:
            raise TypeError('неверный тип аргумента')
        self._chairs = chairs


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        if type(weapons) != dict:
            raise TypeError('неверный тип аргумента')
        self._weapons = weapons

PassengerAircraft('МС-21', 1250, 8000, 12000.5, 1.2)

