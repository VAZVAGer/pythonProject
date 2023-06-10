def subtraction(lst1, lst2):
    list_sub = []
    for i in lst1:
        if i in lst2:
            lst2.remove(i)
        else:
            list_sub.append(i)
    return list_sub


l1 = [1, 2, 2, 3, 4, 5, 6] #2 3 4
l2 = [5, 6, 7, 8, 1, 2,2 ]
print(subtraction(l1, l2))
