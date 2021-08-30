from random import randint

with open('numbers.txt', 'w+', encoding='utf-8') as num:
    num.write(' '.join([str(randint(1, 100)) for _ in range(20)]))
    num.seek(0)
    print(f'Сумма чисел: {sum(map(int, num.readline().split()))}')