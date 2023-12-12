matrix = [["X", " ", "X"],
          [" ", "X", "0"],
          ["X", "X", "X"]]


def is_human_win():
    count_lict = []
    l = 0
    s = 0
    d = 0
    d_ = -1
    for line in matrix:  # Перевіряемо строки
        if "0" not in line and " " not in line:
            print("True")
            return
        else:
            pass
    while s != len(matrix):  # Перевіряємо стовпчики
        while l != len(matrix):
            if matrix[l][s] == 'X':
                count_lict.append(True)
            else:
                count_lict.append(False)
            l += 1
        s += 1
        l = 0
        if False not in count_lict:
            print("True")
            return
        count_lict = []
    for nom, line in enumerate(matrix): # Ліва діагональ
        if line[nom] == "X":
            count_lict.append(True)
        else:
            count_lict.append(False)
    if False not in count_lict:
        print("True")
        return


    print("False")
    return


is_human_win()