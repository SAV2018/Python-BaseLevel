'''
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
'''

class Warehouse:
    ''' Склад '''
    equipments = dict()

    def add_Equipment(self, *arg):
        pass

    def sub_Equipment(self, *arg):
        pass



class OfficeEquipment:
    ''' Оргтехника '''

    def __init__(self, model, price, dpi, paper_size):
        self.model = model
        self.price = price
        self.dpi = dpi
        self.paper_size = paper_size

class Printer(OfficeEquipment):
    ''' Принтер '''

    def __init__(self, model, price, dpi, paper_size, type):
        self.type = type
        super.__init__(model, price, dpi, paper_size)


class Scanner(OfficeEquipment):
    ''' Сканер '''

    def __init__(self, model, price, dpi, paper_size):
        self.dpi = dpi
        super.__init__(model, price, dpi, paper_size)


class Copier(OfficeEquipment):
    ''' Копир '''

    def __init__(self, model, price, dpi, paper_size, print_speed, monthly_print_volume):
        self.print_speed = print_speed
        self.monthly_print_volume = monthly_print_volume
        super.__init__(model, price, dpi, paper_size)



