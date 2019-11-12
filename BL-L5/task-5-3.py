'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

try:
    with open('employees.txt') as f:
        employees = f.readlines()
        print('\n------------------------------\nEnployees with salary < 20 000\n------------------------------')

        av_salary = 0
        for employee in employees:
            name, salary = employee.split()
            av_salary += float(salary)

            if float(salary) < 20000:
                print(f'{name}')

    print('------------------------------')
    print(f'Average salary: {av_salary/len(employees):.2f}')

except FileNotFoundError:
    print('\nError: file not found.')
except IOError:
    print('\nError: input-output error.')