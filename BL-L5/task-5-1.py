'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''
import datetime

# инициализация пременных
filename = 'records.log'    # название лог-файла
records = []                # список новых записей

# ввод новых записей
print('\nAdd new records (press Enter to exit): ')
while True:
    record = input(' > ')
    if record == '':    # если пустая строка - выход из цикла
        break
    else:
        records.append(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} {record}\n')

if records != '':   # если список новых записей не пуст
    # добавляем новые записи в файл
    with open(filename, 'a') as f:
        f.writelines(records)

# выводим кол-во добавленных записей
print(f'{len(records)} records added.')

# выводим все записи из файла лога
print(f'\n------------------------------------\n{filename}\n------------------------------------')
with open(filename) as f:
    for record in f.readlines():
        print(record, end='')
    else:
        print('------------------------------------')