'''
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationary:
    title = None

    def __init__(self):
        print(self.title)

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationary):

    def __init__(self):
        self.title = 'Ручка'
        super().__init__()

    def draw(self):
        print('Рисуем ручкой.')

class Handle(Stationary):

    def __init__(self):
        self.title = 'Маркер'
        super().__init__()

    def draw(self):
        print('Рисуем маркером.')

class Pencil(Stationary):

    def __init__(self):
        self.title = 'Карандаш'
        super().__init__()

    def draw(self):
        print('Рисуем карандашом.')

pen = Pen()
pencil = Pencil()
handle = Handle()

print()
pen.draw()
pencil.draw()
handle.draw()