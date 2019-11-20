'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
'''

class OwnError(Exception):
    def __init__(self, message):
        self.message = message

while True:
    print('\nВведите делимое и делитель: ')
    x = input('> ')
    y = input('> ')

    try:
        x = float(x)
        y = float(y)

        if y == 0:
            raise OwnError('Ошибка: делитель не может быть равен 0.')

    except ValueError:
        print('Ошибка: введено некорректное значение.')
    except OwnError as err:
        print(err)
    else:
        print(f'{x}/{y} = {x/y:.2f}')

    if (input('\nPress <Enter> to continue or any key to exit...') != ''):
        break