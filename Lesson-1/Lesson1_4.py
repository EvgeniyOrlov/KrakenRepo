n = int(input('Введите целое положительное число'))
bigger = 0

while n > 0:
    i = n % 10
    if i > bigger:
        bigger = i
    n //= 10

print(f'Наибольшая цифра = {bigger}')
