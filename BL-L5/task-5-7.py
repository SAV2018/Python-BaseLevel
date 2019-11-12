'''
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
'''

import json

try:
    with open('firms.txt') as f:
        results = {}    # инициализируем словарь
        profits = 0     # инициализируем переменную для подсчёта прибыли
        i = 0           # счетчик прибыльных фирм

        for line in f:
            # разбираем строку
            firm, ownership_type, income, costs = line.split()

            # считаем фин. результат
            result = int(income) - int(costs)
            results[firm] = result

            if result >= 0: # если не убыток
                profits += result
                i += 1

        # создаём файл с данными в JSON
        # собираем данные в список
        fin_list = [results, {'average_profit': profits / i}]
        # пакуем в JSON и пишем в файл
        with open('firms.json', 'w') as jf:
            json.dump(fin_list, jf, ensure_ascii = False)

        print('\nFile "firms.json" created successfully!')

except IOError:
    print('IO error.')
except ValueError:
    print(f'Incorrect money value in line #{i}')