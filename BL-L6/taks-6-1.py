'''
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 сек., второго (желтый) — 2 сек., третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''

from time import sleep

class TrafficLight:
    __color = 0

    def running(self):
        # [красный, жёлтый, зелёный]
        lights = [
                    {
                        'name': 'красный',
                        'color': '\x1b[41m',
                        'delay': 7
                    },
                    {
                        'name': 'жёлтый',
                        'color': '\x1b[43m',
                        'delay': 2
                    },
                    {
                        'name': 'зелёный',
                        'color': '\x1b[42m',
                        'delay': 5
                    }
                ]

        print('\nИмитация работы светофора:\n')

        while True:
            # формируем строку вывода (светофор)
            s = ''
            for i in range(3):
                if i == self.__color:
                    s += f'({lights[self.__color]["color"]}   \x1b[0m)'
                else:
                    s += '(   )'

            print(f'\r{s}', end='')
            # устанавливаем задержку
            sleep(lights[self.__color]["delay"])
            # меняем цвет
            self.__color = (self.__color + 1) % 3

lights = TrafficLight()
lights.running()