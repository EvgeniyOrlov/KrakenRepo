from functools import reduce


def mlt(s_1, s_2):
    return s_1 * s_2


my_lst = [el for el in range(100, 1001, 2)]
print(reduce(mlt, my_lst))
