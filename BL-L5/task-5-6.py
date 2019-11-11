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
    '''
    Суммирование часов по предмету
    :param hlist: список часов (лекции, практ., лаб.)
    :return: сумма часов
    '''
    hours = 0

    for h in hlist:
        if (h != '—'): # если параметр не пропущен
            try:
                hours += int(h)
            except ValueError:
                print(f'\nError: incorrect value of hours "{h}"', end='')
                raise
    return hours

filename = 'subjects.lst'
try:
    with open(filename) as f:
        dict = {}   # инициализируем словарь

        # обрабатываем файл по строкам
        for i, item in enumerate(f, 1):
            print(item, end='')

            # удаляем лишние символы из строки
            signatures = [':', '(л)', '(пр)', '(лаб)']
            for signature in signatures:
                item = item.replace(signature, '')

            # разбиваем строку на две части (название предмета и кол-во часов)
            subject, *hours = item.split()

            # добавляем значение в словарь
            try:
                dict[subject] = sum_hours(hours)
            except ValueError:
                print(f' in line #{i}')
                exit(1)

    print(f'\n\n{dict}')

except FileNotFoundError:
    print(f'Error: File "{filename}" not found.')
except IOError:
    print('Error: input-output error.')

