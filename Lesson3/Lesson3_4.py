def my_func(x, y):
    return x ** y


num1, num2 = float(input('Введите число действительное положительное число: ')),\
             int(input('Введите  целое отрицательное число: '))

print(f'{my_func(num1, num2):.3f}')
