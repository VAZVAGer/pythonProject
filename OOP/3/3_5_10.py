class Box:
    def __init__(self):
        self.list_things = []

    def add_thing(self, obj):
        self.list_things.append(obj)


    def get_things(self):
        return self.list_things


    def __eq__(self, other):
        if len(self.list_things) != len(other.list_things):
            return False
        a = []
        cop_box = other.list_things.copy()
        for b1 in self.list_things:
            for b2 in cop_box:
                if b1 == b2:
                    a.append(True)
                    cop_box.remove(b2)
        if len(self.list_things) == len(a):
            return True
        else:
            return False


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2
print(res)