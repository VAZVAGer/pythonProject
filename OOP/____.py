def subtraction(lst1, lst2):
    sub_list = []
    work_list = lst1.copy()
    work_list2 = lst2.copy()
    for i, zn1 in enumerate(lst1):
        flag = []
        for ii, zn2 in enumerate(work_list2):
            flag.append(type(zn1) == type(zn2) and zn1 == zn2)
            if type(zn1) == type(zn2) and zn1 == zn2:
                work_list2[ii] = None
                break

        if True not in flag:
            sub_list.append(zn1)
    return sub_list





l1 = [1, 0, True, False, 5.0, True, 1, True, -7.87] #[0, 5.0, 1, True, -7.87]
l2 = [10, True, False, True, 1, 7.87]
print(subtraction(l1, l2))
