my_lst = input('Enter a few words separated by a space: ').split(' ')

for i in range(len(my_lst)):
    print(f'{i+1}. {my_lst[i]:.10s}')