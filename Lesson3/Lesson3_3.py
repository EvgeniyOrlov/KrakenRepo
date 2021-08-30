def my_func(n1, n2, n3):
    return (n1 + n2 + n3) - min(n1, n2, n3)


num1, num2, num3 = int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: '))

print(my_func(num1, num2, num3))
