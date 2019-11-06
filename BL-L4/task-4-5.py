'''
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

from functools import reduce

def multiply_list(item_1, item_2):
    return item_1 * item_2

new_list = [i for i in range(100, 1001) if i % 2 == 0]

print(f'\n{new_list}')
print(reduce(multiply_list, new_list))