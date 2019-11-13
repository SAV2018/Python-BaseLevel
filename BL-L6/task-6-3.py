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
    name = None
    surname = None
    position = None
    _income = None

    def __init__(self, name, surname, position):
        Worker.name = name
        Worker.surname = surname
        Worker.position = position


class Position(Worker):

    def __init__(self, name, surname, position, dict):
        super().__init__(name, surname, position)
        Worker._income = dict

    def get_full_name(self):
        return Worker.name + ' ' + Worker.surname

    def get_total_income(self):
        return Worker._income['wage'] + Worker._income['bonus']


position_1 = Position('John', 'Walter', 'manager', {'wage': 1000, 'bonus': 100})
position_2 = Position('Artur', 'Doyle', 'director', {'wage': 2500, 'bonus': 500})

print(position_1.get_full_name())
print(position_1.get_total_income())