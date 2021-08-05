mnth_list = ['Januaru', 'February', 'March', 'April', 'May', 'June', 'Jule',
             'August', 'September', 'October', 'November', 'December']

ssn_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autmn'}

num = int(input('Enter the number of the month: '))

if 0 < num < 3 or num == 12:
    print(f"It's {ssn_dict.get(1)}, {mnth_list[num-1]}.")
elif 2 < num < 6:
    print(f"It's {ssn_dict.get(2)}, {mnth_list[num - 1]}.")
elif 5 < num < 9:
    print(f"It's {ssn_dict.get(3)}, {mnth_list[num - 1]}.")
elif 8 < num < 12:
    print(f"It's {ssn_dict.get(4)}, {mnth_list[num - 1]}.")
else:
    print('Error, invalid input')


