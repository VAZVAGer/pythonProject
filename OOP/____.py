a = ((1, 2),)
b = ((7, 9),)
c = ((8, 33),)
a = a + b + c
print(a)
l = 0
for i in range(len(a)-1):
    print(a[i:i+2])
    time_t = (a[i:i+2])
    l += ((time_t[-1][0] - time_t[0][0])**2 + (time_t[-1][-1] - time_t[0][-1])**2)
print(l)