from itertools import count, cycle
from random import randint

my_lst = [randint(5, 50) for _ in range(10)]
s = 0

for el in count(100):
    if el > 110:
        break
    else:
        print(el)

for el in cycle(my_lst):
    if s > 10:
        break
    print(el)
    s += 1
