# n, m = map(int, input().split())
# words = list(map(str, input().split()))
# lst_in = list(map(str.strip, sys.stdin.readlines()))
matrix = [4, 5, 2, 0, 6, 3, -56, 3, -1]
ind = len(matrix)
n = 0
while n != ind:
    n += 1
    for index_1 in range(ind - 1):
        znachenie_1 = matrix[index_1]
        if matrix[index_1] > matrix[index_1 + 1]:
            matrix[index_1], matrix[index_1 + 1] = matrix[index_1 + 1], matrix[index_1]
print(*matrix)