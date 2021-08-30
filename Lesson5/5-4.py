translate_dct = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('new_file.txt', 'w', encoding='utf-8') as new_file:
    with open('text_4.txt', 'r', encoding='utf-8') as text_4:
        new_file.writelines([i.replace(i.split()[0], translate_dct.get(i.split()[0])) for i in text_4])
