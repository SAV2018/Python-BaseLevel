'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (2-х матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
'''

matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

class Matrix:
    ''' Матрица '''

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = '\n'
        for line in self.matrix:
            s += '|'
            for i in line:
                s += f' {i} '
            s += '|\n'
        return s

    def __add__(self, other):
        # проверка размерности матриц
        if len(self.matrix) == len(other.matrix) or len(self.matrix[0]) == len(other.matrix[0]):
            # складываем матрицы поэлементно
            m = []
            for i in range(len(self.matrix)):
                m.append([])
                for j in range(len(self.matrix[0])):
                    m[i].append(self.matrix[i][j] + other.matrix[i][j])
            return Matrix(m)

m1 = Matrix(matrix_1)
m2 = Matrix(matrix_2)

print('\nИсходные матрицы:\n', m1, m2)
print('Сумма 2-х матриц:\n', m1 + m2)