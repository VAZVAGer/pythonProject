class Animal:
   def __init__(self, name, old):
       self.name = name
       self.old = old

class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weidht = weight

    def get_info(self):
        return f"{self.name}: {self.old}, {self.color}, {self.weidht}"

class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size
    def get_info(self):
        return f"{self.name}: {self.old}, {self.color}, {self.weidht}, {self.breed}, {self.size}"