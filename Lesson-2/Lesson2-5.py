my_lst = [9, 5, 3, 3, 1]

while True:
    num = int(input('Введите натуральное чисто (от 1 до 9): '))
    for i in range(len(my_lst)):
        if my_lst[i] < num:
            my_lst.insert(i, num)
            break

    ch = input('Желаете ввести следующее число? Введите "да" или "нет".')
    if ch.lower() == 'да':
        continue
    else:
        break

print(f'Ваш список:\n{my_lst}')
