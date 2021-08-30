
my_file = open('my_file.txt', 'w', encoding='UTF-8')
while True:
    data = input('Введите свои даные для записи в журнал, или нажмите "Enter" для завершения:')
    if data:
        my_file.write(f'{data}\n')
    else:
        break
my_file.close()
