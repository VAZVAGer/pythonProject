# Калькулятор
while True:
    a = int(input())
    operation = input('+ - * /,')
    b = int(input())
    result = 0

    if operation == '+':
        result = a + b
        print('Результат:', result)
    elif operation == '-':
        result = a - b
        print('Результат:', result)
    elif operation == '*':
        result = a * b
        print('Результат:', result)
    elif b == 0:
        print("Болван, на ноль делить НЕЛЬЗЯ!!!")
    elif operation == '/':
        result = a / b
        print('Результат:', result)

