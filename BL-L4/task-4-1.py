'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

from sys import argv

scriptname, name, worktime, rate_per_hour, bonus = argv
print(f'Payroll for {name}: {worktime} hours worked, rate ${rate_per_hour} per hour, bonus ${bonus}')

try:
    print(f'\nSalary of {name}: ${round(float(worktime) * float(rate_per_hour) + float(bonus), 2):.2f}')
except ValueError:
    print('Error: Incorrect value of parameter')