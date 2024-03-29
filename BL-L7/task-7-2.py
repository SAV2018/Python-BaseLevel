'''
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import abstractmethod

class Clothes:
    ''' Одежда '''
    type = None

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_consumption(self):
        pass

class Coat(Clothes):
    ''' Пальто '''

    def __init__(self, size, name=''):
        self.type = 'Coat'
        self.size = size
        super().__init__(name)

    @property
    def get_consumption(self):
        return self.size / 6.5 + 0.5

class Jacket(Clothes):
    ''' Пиджак '''

    def __init__(self, growth, name=''):
        self.type = 'Jacket'
        self.growth = growth
        super().__init__(name)

    @property
    def get_consumption(self):
        return self.growth * 2 + 0.3


coat = Coat(48, 'Henderson')
jacket = Jacket(6, 'Tom Taylor') # in feet
jack_2 = Jacket(5.6)

print(f'\n{coat.type} "{coat.name}": {coat.get_consumption:.2f}\n{jacket.type} "{jacket.name}":'
      f' {jacket.get_consumption:.2f}\n{jack_2.type}: {jack_2.get_consumption:.2f}')