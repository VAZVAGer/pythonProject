matrix = [[" ", "X", "X"],
          ["X", " ", "0"],
          ["X", "X", " "]]


def is_human_win():
    count_lict = []
    l = 0
    s = 0
    for line in matrix:
        if "0" not in line and " " not in line:
            print("True")
            return
        else:
            pass
    while s != len(matrix):
        while l != len(matrix):
            if matrix[l][s] == 'X':
                count_lict.append(True)
            else:
                count_lict.append(False)
            l += 1
        s += 1
        l = 0
        count_lict = []
    if False not in count_lict:
        print("True")
        return

    print("False")
    return

is_human_win()
