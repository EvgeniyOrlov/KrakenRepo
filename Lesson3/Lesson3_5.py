def summ():
    s = 0
    while True:
        my_lst = input('Введите числа через пробел, или "q" для завершения работы: ').split(' ')
        s1 = 0
        for i in my_lst:
            if i.lower() == 'q':
                return s
            elif i.isdigit():
                s += int(i)
                s1 += int(i)
            else:
                print('Введите числа или "q" для выхода')
        print(f'{s1}({s})')


summ()
