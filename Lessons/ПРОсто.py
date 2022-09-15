# list1 = list(map(int, input().split()))
# a, b = map(int, input().split())

from string import ascii_lowercase, ascii_uppercase
import random

N = int(input())


def password_generator(number_of_digits):
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    N = 0
    while N <= number_of_digits - 1:
        random.seed()
        indx = random.randint(0, len(chars) - 1)
        N += 1
        yield chars[indx]


s = password_generator(N)
for x in s:
    print(x, end="")
print()
s = password_generator(N)
for x in s:
    print(x, end="")
print()
s = password_generator(N)
for x in s:
    print(x, end="")
print()
s = password_generator(N)
for x in s:
    print(x, end="")
print()
s = password_generator(N)
for x in s:
    print(x, end="")
print()