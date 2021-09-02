from random import choice


class Car:
    go_turn = ['север', 'юг', 'запад', 'восток']

    def __init__(self, n, clr, spd, isp=False):
        self.speed = spd
        self.color = clr
        self.name = n
        self.is_police = isp

    def go(self):
        print(f'Автомобиль {self.name}, поехал.')

    def stop(self):
        print(f'Автомобиль {self.name}, остановился.')

    def turn(self):
        print(f'Автомобиль {self.name}, повернул на {choice(self.go_turn)}.')

    def car_speed(self):
        print(f'Скорость автомобиля {self.name}: {self.speed}.')


class TownCar(Car):

    def car_speed(self):
        return f'{self.name}: скорость - {self.speed}. Превышение скорости!' if self.speed > 60 else super().car_speed()


class SportCar(Car):
    def car_speed(self):
        return f'{self.name}: скорость - {self.speed}. Превышение скорости!' if self.speed > 90 else super().car_speed()


class WorkCar(Car):

    def car_speed(self):
        return f'{self.name}: скорость - {self.speed}. Превышение скорости!' if self.speed > 40 else super().car_speed()


class PoliceCar(Car):

    def __init__(self, spd, clr, n, isp=True):
        super().__init__(spd, clr, n, isp)

    def car_speed(self):
        return f'Полицейский {self.name}: скорость - {self.speed}.'


town = TownCar('Skoda', 'серая', 90)
work = WorkCar('MAN', 'желтый', 30)
sport = SportCar('Ferrari', 'красная', 170)
police = PoliceCar('Ford', 'синий', 70)

cars = [town, work, sport, police]

for i in cars:
    i.go()
    print(i.car_speed())
    i.turn()
    i.stop()
    print()
