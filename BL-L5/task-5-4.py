'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

numerals_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}
filename = 'numerals'

# читаем из файла
with open(f'{filename}.eng') as f:
    numerals = f.readlines()

    # меняем английские числительные на русские
    numerals_rus = []
    for element in numerals:
        key, *others = element.split()  # выделяем первое слово в строке (англ.)
        numerals_rus.append(element.replace(key, numerals_dict[key])) # меняем это слово в строке на русское из словаря

# сохраняем в новый файл
with open(f'{filename}.rus', 'w') as f:
    f.writelines(numerals_rus)