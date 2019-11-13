'''
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т.
'''


class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        Road._length = length
        Road._width = width

    def get_weight(self):
        weight_per_meter = 25 # масса 1 кв. метра асфальта толщиной 1 см.
        thickness = 5 # толщина асфальта в см.

        return Road._length * Road._width * weight_per_meter * thickness

while True:
    try:
        print('\nВведите параметры дороги: ')
        road = Road(float(input('длину\t> ')), float(input('ширину\t> ')))
    except ValueError:
        print('Incorrect value')
        continue

    print(f'\nМасса асфальта: {road.get_weight():.01f} кг.')

    if input('\nPress Enter to continue, any key to exit.') != '':
        break  # завершение работы