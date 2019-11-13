'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker:
    ''' Сотрудник '''
    name = None
    surname = None
    position = None
    _income = None

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    ''' Должность '''
    def __init__(self, name, surname, position, dict):
        super().__init__(name, surname, position)
        self._income = dict

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


positions = [
            Position('John', 'Walter', 'manager', {'wage': 1000, 'bonus': 100}),
            Position('Artur', 'Doyle', 'director', {'wage': 2500, 'bonus': 500})
            ]

for position in positions:
    print(f'\n{position.get_full_name()}')
    print(position._income, end='')
    print(' =>', position.get_total_income())