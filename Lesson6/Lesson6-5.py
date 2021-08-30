class Stationery:

    def __init__(self, title='Параметр'):
        self.title = title

    def draw(self):
        return self.title


class Pen(Stationery):
    def draw(self):
        print(f'Рисование ручкой {self.title}!')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисование {self.title} карандашом!')


class Marker(Stationery):
    def draw(self):
        print(f'Рисование {self.title} маркером!')


s = Stationery()
pen = Pen('Pilot')
pencil = Pencil('цветным')
marker = Marker('огромным')

stat_lst = [s, pen, pencil, marker]

for i in stat_lst:
    i.draw()
