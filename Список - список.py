# while True
#    a = input("Введите выражение: ")
#    b = eval(a)
#   print("Результат", b)

expression = input("Ввод:")
import re

numbers = re.split(r"[-,+, *,/,]", expression)
symbols = re.findall(r"[-,+, *,/,]", expression)
print(numbers)
print(symbols)
c = list()
f = list()
for a in numbers:
    b = float(a)
c.append(b)
print(b)
