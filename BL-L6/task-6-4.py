'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''

class Car:
    ''' Автомобиль '''
    _speed = None
    _color = None
    _name = None
    _is_police = False

    def __init__(self, name, color):
        self.name = name
        self.color = color
        print(f'Новая машина: {self.name} (цвет {self.color})')

    def go(self):
        print(f'{self.name}: Машина поехала.')

    def stop(self):
        print(f'{self.name}: Машина остановилась.')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"налево" if direction==0 else "направо"}.')

    def show_speed(self, speed):
        print(f'{self.name}: Скорость автомобиля: {speed}.')


class TownCar(Car):
    ''' Городской автомобиль '''
    def show_speed(self, speed):
        if speed > 60:
            print(f'{self.name}: Скорость автомобиля: {speed}. Превышение скорости!')
        else:
            super().show_speed(speed)


class WorkCar(Car):
    ''' Грузовой автомобиль '''
    def show_speed(self, speed):
        if speed > 40:
            print(f'{self.name}: Скорость автомобиля: {speed}. Превышение скорости!')
        else:
            super().show_speed(speed)


class SportCar(Car):
    ''' Спортивный автомобиль '''


class PoliceCar(Car):
    ''' Полицейский автомобиль '''
    def __init__(self, name, color):
        super().__init__(name, color)
        self.is_police = True


police_car = PoliceCar('"Полицайка"', 'белый')
police_car.go()
police_car.show_speed(80)
police_car.turn(0)
police_car.stop()
print()

work_car = WorkCar('"Грузовичок"', 'хаки')
work_car.go()
work_car.turn(1)
work_car.show_speed(40)
work_car.turn(0)
work_car.show_speed(45)
work_car.stop()

print('\x1b[1m{}')
sport_car = SportCar('"Спортивка"', 'красный')
sport_car.go()
sport_car.turn(0)
sport_car.show_speed(120)
sport_car.stop()
print()

town_car = TownCar('"Малютка"', 'жёлтый')
town_car.go()
town_car.show_speed(50)
town_car.turn(1)
town_car.turn(0)
town_car.show_speed(66)
town_car.stop()

print(f'\nМашина {town_car.name} (цвет {town_car.color})')
print(f'Машина {police_car.name} (цвет {police_car.color})')