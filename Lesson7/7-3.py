class Cell:
    def __init__(self, n):
        self.n = n

    def make_order(self, row):
        return '\n'.join(['*' * row for _ in range(self.n // row)]) + '\n' + '*' * (self.n % row)

    def __str__(self):
        return f'{self.n}'

    def __add__(self, other):
        print('Сумма клеток:')
        return Cell(self.n + other.n)

    def __sub__(self, other):
        print('Разность клеток:')
        return Cell(self.n - other.n)

    def __mul__(self, other):
        print('Произведение клеток:')
        return Cell(self.n * other.n)

    def __floordiv__(self, other):
        print('Целочисленное деление клеток:')
        return Cell(self.n // other.n)


c_1 = Cell(35)
c_2 = Cell(27)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 // c_2)
print(c_2.make_order(5))
