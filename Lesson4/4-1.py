from sys import argv


def division(s_1, s_2, s_3):
        s_1, s_2, s_3 = int(s_1), int(s_2), int(s_3)
        print(f"ЗП составила: {s_1 * s_2 + s_3} у.е.")


try:
    script_name, production, per_hour, prize = argv

    print("Имя скрипта: ", script_name)
    print("Выработка в часах: ", production)
    print("Ставка в час: ", per_hour)
    print("Премия: ", prize)

    division(production, per_hour, prize)
except ValueError:
    print('Err! Please, input 3 values.')



