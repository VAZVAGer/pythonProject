# list1 = list(map(int, input().split()))
# a, b = map(int, input().split())

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
list1.sort()
list2.sort(reverse=True)
zi = zip(list1, list2)
for a, b in zi:
    print(a + b, end=" ")

