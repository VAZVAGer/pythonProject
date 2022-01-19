class Person:
    object_number = 0

    def __init__(self, name, surname, p_of_b,year_of_birth ):
        self.name = name
        self.surname = surname
        self.p_of_b = p_of_b
        self.year_of_birth = year_of_birth
        Person.object_number += 1

    def print_info(self, n):
        for i in range(n):
            print(f'Name: {self.name}, Surmane: {self.surname}, p_of_b: {self.p_of_b}')

    def age (self, y):
        print("Возраст", y-self.year_of_birth)

p1 = Person("Вася", "Коллов","Саратов", 1991)
p2 = Person("Петя", "Пупкин","Днепр", 1854)
p3 = Person("Ектерина", "Быкова","Екатеронослав", 1988)
p3.print_info(3)
p1.age(2021)
p2.age(2021)
p3.age(2021)
print(p3.name)
print(Person.object_number)