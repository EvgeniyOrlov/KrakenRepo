def division(n_1, n_2):
    try:
        print(f'Результат: {int(n_1 / n_2)}')
    except ZeroDivisionError:
        print('Err')


n1 = int(input('Введите делитель: '))
n2 = int(input('Введите делимое: '))
division(n1, n2)
