'''
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
'''
from itertools import count, cycle

# а)
ilist = ['one', 'two', 'three', 555]

print(f'\n(a) ------------------------------------------ \n\n{ilist}')
for i, item in enumerate(cycle(ilist)):
    if i > 13:
        break
    print(item, end=' | ')

print('... That\'s enough.')

# б)
print('\n(b) ------------------------------------------')
action = ''
while action == '':
    try:
        start_num = int(input('\nEnter start number: '))
        final_num = int(input('Enter final number: '))

        if start_num > final_num:
            print('Incorrect value')
        else:
            for i in count(start_num):
                if i > final_num:
                    break
                print(i)

            print('That\'s enough.')

    except ValueError:
        print('Incorrect value')


    action = input('\nPress Enter to continue or any key to exit...')