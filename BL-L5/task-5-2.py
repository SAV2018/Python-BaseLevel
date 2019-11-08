'''
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк и
количества слов в каждой строке.
'''

# инициализация пременных
filename = 'records.log'    # название файла

with open(filename) as f:
    lines = f.readlines()
    print(f'\n{len(lines)} lines in file "{filename}"\n')

    for i, line in enumerate(lines, 1):
        words = line.split() # разбиваем строку на слова
        print(f'{len(words)} words in line {i}\t{words}')    # считаем кол-во слов в строке