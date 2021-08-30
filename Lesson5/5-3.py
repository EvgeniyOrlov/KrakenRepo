text_3 = open("text_3.txt", "r", encoding="utf-8")
lst = []
salary = 0
less20 = []
count = 0

for i in text_3:
    lst.append(i[:len(lst) - 1])
    a = lst[0].split(' ')
    if float(a[1]) < 20000:
        less20.append(a[0])
    salary += float(a[1])
    count += 1
    lst = []

print('Оклады менее 20000р. имеют следующие сотрудники:', end=' ')
print(*less20, sep=', ', end='.\n')
print(f'Средний зароботок составил: {salary / count}р.')
text_3.close()


# _________________________тренируюсь с разбором дз___________________

# with open('text_3.txt', 'r', encoding='utf-8') as text:
#     eml_dct = {i.split()[0]: float(i.split()[1]) for i in text}
#     print(f'Средний зароботок составил: {(sum(eml_dct.values()) / len(eml_dct))}\n'
#           f'Оклады менее 20000р. имеют следующие сотрудники:{[s[0] for s in eml_dct.items() if s[1] < 20000]}.')
