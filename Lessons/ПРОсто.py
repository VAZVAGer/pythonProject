# list1 = list(map(int, input().split()))
# a, b = map(int, input().split())

list1 = ['Лена', 'Енисей', 'Волга', 'Дон']
s_list = sorted(list1, key=len, reverse=True )
print(s_list)
