'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

from datetime import datetime

class Date:
    ''' Класс для работы с датой '''

    def __init__(self, date):
        '''
        :param date: строка формата «день-месяц-год» (DD-MM-YYYY)
        '''
        self.date = Date.str_to_date()

    @classmethod
    def str_to_date(cls, date):
        ''' Перевод даты в виде строки в datetime '''
        d = None
        try:
            d = datetime.strptime(date, "%d-%m-%Y")
        except (ValueError, TypeError) as err:
            print(f'Error: {err}')

        return d

    @staticmethod
    def is_valid(date):
        ''' Функция проверки даты'''
        return (Date.str_to_date(date) != None)


def check_date(date):
    ''' Проверка и вывод введённой и разобранной даты (либо ошибки) '''
    print(f'\nДата: {date}')
    if (Date.is_valid(date)):
        d = Date.str_to_date(date)
        print(f'Day: {d.day} {type(d.day)}\nMonth: {d.month} {type(d.month)}\nYear: {d.year} {type(d.year)}')


# список дат для проверки
dates = '10-10-2019', '1-12-2000', '20.10.2005', '', '100-10-2019', '01-kj-2019', '32-10-2000', '10-13-2001', 444

#  проверяем даты по списку
for date in dates:
    check_date(date)

# ввод произвольной даты
while True:
    date = input('\nEnter date (DD-MM-YYYY): ')
    check_date(date)

    if (input('\nPress <Enter> to continue or any key to exit...') != ''):
        break