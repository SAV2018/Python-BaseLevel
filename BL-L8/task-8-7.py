'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''

class ComplexNumber:
    ''' Комплексное число '''

    def __init__(self, n):
        self.n = complex(n)

    def __add__(self, other):
        return self.n + other.n

    def __mul__(self, other):
       return self.n * other.n


while True:
    print('\nВведите два комплексных числа: ')
    try:
        x = ComplexNumber(input('x > '))
        y = ComplexNumber(input('y > '))
    except ValueError:
        print('Ошибка: введено некорректное значение.')
    else:
        # Вывод результатов
        print(f'\nx + y = {x + y}')
        print(f'x * y = {x * y}')

    if (input('\nPress <Enter> to continue or any key to exit...') != ''):
        break