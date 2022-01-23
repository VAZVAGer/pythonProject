#my_list = [1, 1, 2, 5, 10, 10, 10]  # 1+2+5+10=18
#set_1 = set(my_list)

#c = 0
#for sam in set_1:
 #   c += sam

#print(c)

#print(sum(set(my_list)))

s = {1, 3, 5., 777, 545}
l = [777, 7]

def my_fank(s, l):
    if len(l) > len(s):
        return False
    for list_el in l:
        if list_el not in s:
            return  False

    return True

print(my_fank(s, l))
