'''
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика:   100(л)   50(пр)   20(лаб).
Физика:   30(л)   —   10(лаб)
Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

def sum_hours(hlist):
    hours = 0
    for h in hlist:
        if (h == '—'):
            continue
        else:
            try:
                hours += int(h)
            except ValueError:
                print(f'Incorrect value of hours "{h}"')
    return hours

filename = 'subjects.lst'
try:
    with open(filename) as f:
        for item in f:
            print(item)

            # удаляем 
            signatures = [':', '(л)', '(пр)', '(лаб)']
            for signature in signatures:
                item = item.replace(signature, '')
            subject, *hours = item.split()
            print(subject, hours)

            print(f'Сумма часов: {sum_hours(hours)}')


except FileNotFoundError:
    print(f'Error: File "{filename}" not found.')
except IOError:
    print('Error: input-output error.')