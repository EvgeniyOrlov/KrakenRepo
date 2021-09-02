class Worker:

    def __init__(self, n, sn, pos, inc_d):
        self.name = n
        self.second_name = sn
        self.position = pos
        self._income = inc_d


class Position(Worker):

    def get_full_name(self):
        print(f'Worker fullname: {self.name} {self.second_name}.')

    def get_total_income(self):
        print(f'Total income: {sum(self._income.values())}.')


x = Position('Sergey', 'Smirnov', 'Senior Developer', {'wage': 150000, 'bonus': 50000})
x.get_full_name()
x.get_total_income()
