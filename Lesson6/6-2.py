class BuildRoad:
    def __init__(self, ln, wd):
        self._length = ln
        self._width = wd

    def mass_of_road(self, m, t):
        print(f'Mass of road: {self._length * self._width * m * t / 1000} tons.')


s = BuildRoad(int(input('Input length of road(m):')), int(input('Input width of road(m):')))
s.mass_of_road(int(input('Input mass on sq. meter(kg):')), int(input('Input thickness of road(sm):')))
