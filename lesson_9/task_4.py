from random import randint


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Поехали на {self.name}')

    def stop(self):
        print(f'Остановились на {self.name}')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        return randint(0, self.speed)


class TownCar(Car):
    """Town car"""

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        speed = super().show_speed()
        if speed > 60:
            print(f'Превышение скорости на {speed - 60}')


class SportCar(Car):
    """Sport car"""


class WorkCar(Car):
    """Work car"""

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        speed = super().show_speed()
        print(f'Скорость {speed} км/ч')
        if speed > 40:
            print(f'Превышение скорости на {speed - 40} км/ч')


class PoliceCar(Car):
    """Police car"""

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


work_car_1 = WorkCar(110, 'white', 'Лошадка')
work_car_1.go()
work_car_1.turn('налево')
work_car_1.show_speed()
work_car_1.stop()
