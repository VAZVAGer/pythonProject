cord = [3, 5, 8, 9, 12]
def set_coords(*args):
    for i, n in enumerate(args[:len(cord)]):
        cord[i] = n

set_coords(4,)
print(cord)
