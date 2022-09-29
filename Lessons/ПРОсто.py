# list1 = list(map(int, input().split()))
# a, b = map(int, input().split())
a = input()
key = 123
for x in a:
    print(chr(ord(x) ^ key), end='')