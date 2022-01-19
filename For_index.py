list = ["Масян", "Каламбур", "какаха", "фокус",5,2108,'GOLF4']

for b in list:
    print(b)
print ('а теперь через индекс:')
for ss in range(len(list)):
    print(list[ss])

print ('Цикл в цикле:')
for www in range(len(list)):
    for mmm in range (www+1):
        print(list[www])