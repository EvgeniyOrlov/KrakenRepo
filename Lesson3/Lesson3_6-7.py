def int_func():
    my_lst = input('Введите предложение латинскими буквами в нижнем регистре(через пробел): ').split(' ')
    for i in my_lst:
        count = 0
        for j in i:
            if 97 <= ord(j) <= 122:
                count += 1
            else:
                break
        if count == len(i):
            print(i.title(), end=' ')


int_func()
