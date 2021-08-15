with open('text_6.txt', 'r', encoding='utf-8') as text_6:
    ln = text_6.readlines()
    for j in ln:
        crt_str = ''.join((i if i in '0123456789' else ' ') for i in j)
        new_crt = [int(i) for i in crt_str.split()]
        print(f'{j.split()[0]} {sum(new_crt)}')
