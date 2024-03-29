'''
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
'''

class NonDigitException(Exception):
    def __init__(self, message):
        self.message = message

elements = []
while True:
    element = input('\nEnter number or <Enter> to exit: ')
    if (element == ''):
        break

    try:
        if not element.isdigit():
            raise NonDigitException('Ошибка: введено не число - не вносится в список.')
        elements.append(int(element))
    except ValueError:
        print('Ошибка: введено некорректное значение.')
    except NonDigitException as err:
        print(err)


print(f'\n{elements}')