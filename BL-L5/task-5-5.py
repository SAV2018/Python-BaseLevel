'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
from random import randint

try:
    # формируем файл с набором случайных чисел
    with open('numbers.txt', 'w') as f:
        f.write(' '.join([str(randint(0, 100)) for i in range(randint(2, 100))]))

    with open('numbers.txt') as f:
        try:
            array = [int(n) for n in f.readline().split()]
            print(array)
            print(f'Sum: {sum(array)}')
        except ValueError:
            print('Incorrect value')

except IOError:
    print('\nIO error.')