my_lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_lst = [my_lst[el] for el in range(1, len(my_lst)) if my_lst[el] > my_lst[el - 1]]

print(new_lst)
