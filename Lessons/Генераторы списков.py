a = ['привет', "мадрид", "така", "каптерка", "лосось", "лом", "ток"]
print(a)
b = [num * 2 for num in range(10, 1, -1) if num % 2 == 0]
print(b)

v = [ fac +'.' for fac in a if len(fac) > 5]
print (v)
