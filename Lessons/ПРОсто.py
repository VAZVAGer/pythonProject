# n, m = map(int, input().split())
# words = list(map(str, input().split()))
# lst_in = list(map(str.strip, sys.stdin.readlines()))
matrix = [8, 11, -53, 2, 10, 11]

n = 0
while n <= len(matrix):
    mini = 0
    maxi = 0
    n += 1
    for vel in matrix[n+1::]:
        vel = mini
        if mini > maxi:
            mini, maxi = maxi, mini



