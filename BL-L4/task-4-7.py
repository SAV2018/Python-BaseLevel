'''
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fibo_gen().
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''

def get_factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
        yield f


while True:
    try:
        n = int(input('\nEnter number: '))

        for i, f in enumerate(get_factorial(n)):
            if i < 15: # выводим только первые 15 значений
                print(f)

    except ValueError:
        print('Incorrect value')

    if (input('\nPress Enter to continue or any key to exit...') != ''):
        break  # завершаем работу скрипта