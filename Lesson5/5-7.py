from json import dump

with open('text_7.txt', 'r', encoding='utf-8') as read_f:
    with open('text_77.json', 'w', encoding='utf-8') as write_f:
        my_dict = {s.split()[0]: int(s.split()[2]) - int(s.split()[3]) for s in read_f}
        avr_profit = []
        for i in my_dict.values():
            if i > 0:
                avr_profit.append(i)
        dump([my_dict, f'Суммарная прибыль: {sum(avr_profit) / len(avr_profit)}'],
             write_f, ensure_ascii=False)
