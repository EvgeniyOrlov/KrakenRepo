profit = int(input('Введите сумму прибыли Вашей компании за последний месяц'))
loss = int(input('Введите сумму убытка Вашей компании за последний месяц'))

n = profit - loss

if n > 0:
    print(f'Прибыль составила: {n}, рентабельность составила {n * 100 / profit:.1f}%')
    num_employees = int(input('Введите количество сотрудников работающих в Вашей компании'))
    print(f'Прибыль на каждого сотрудника составила: {n / num_employees:.3f}')
elif n < 0:
    print(f'Убыток компании равен {n * -1}')
else:
    print(f'Выручка равна издержкам')
