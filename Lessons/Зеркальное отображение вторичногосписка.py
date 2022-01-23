max_masiv = [[1, 2, 3, 4],
             [4, 5, 6, 7],
             [7, 8, 9, 10]]


# Надо зеркально отобразить в [[3,2,1],
#                              [6,5,4],
#                              [9,8,6]]


def zerkal(max_masiv):
    for arr in max_masiv:
        for t in range(len(arr) // 2):
            j = len(arr) - 1 - t
            arr[t], arr[j] = arr[j], arr[t]


zerkal(max_masiv)
print(max_masiv)
