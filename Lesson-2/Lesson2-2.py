my_lst = []

while True:
    how_many = input('Enter the number of items in your list: ')
    if how_many.isdigit():
        how_many = int(how_many)
        break
    else:
        print('Mistake. You must enter an integer, try again')
        continue

for _ in range(how_many):
    values = input('Enter value for your list: ')
    my_lst.append(values)

for i in range(1, (how_many), 2):
    my_lst[i], my_lst[i-1] = my_lst[i-1], my_lst[i]

print(my_lst)