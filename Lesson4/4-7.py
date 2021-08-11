def factorial(n):
    total = 1
    for i in range(n + 1):
        yield total
        total *= i + 1


num = int(input('Введите число для вычисления факториала: '))

for el in factorial(num):
    print(el)
