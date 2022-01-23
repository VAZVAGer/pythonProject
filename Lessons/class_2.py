class Animals:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animals):
    def __init__(self, name, breed):
        Animals.__init__(self, name)
        self.breed = breed

    def bark(self):
        print(f"Dog {self.name} is barking!!!")


class Cat(Animals):
    def meaw(self):
        print(f"{self.name} says meaw")


class Frog(Animals):
    def eat(self):
        print(f"Frog with {self.name} is eating")


d1 = Dog("Тузик", "Серый")
c1 = Cat("Барсик")
f1 = Frog("Царевна_жаба")

d1.bark()
d1.eat()
c1.meaw()
c1.eat()
f1.eat()

