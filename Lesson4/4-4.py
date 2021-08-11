my_lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_lst = []
for el in my_lst:
    count = 0
    for i in my_lst:
        if i == el:
            count += 1
    if count == 1:
        unique_lst.append(el)

print(unique_lst)

# ____________________Вспомнил, после того, как написал 1й вариант______________________________________

# my_lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# unique_lst = [el for el in my_lst if my_lst.count(el) == 1]
# print(unique_lst)
