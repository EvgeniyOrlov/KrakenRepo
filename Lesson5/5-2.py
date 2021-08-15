my_file = open("my_file.txt", "r")
count_str = 0
lst = []

for i in my_file:
    lst.append(i[:len(lst) - 1])
    a = lst[0].split(' ')
    count_str += 1
    print(f'Количество слов в {count_str} строке: {len(a)}')
    lst = []

print(f'Количество строк в файле: {count_str}')

my_file.close()
