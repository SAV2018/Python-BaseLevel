'''
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
'''

num_list = [100, 5, 11, 0, 5, 13, 44, 67, 5, 1, 100, 80, 99, 99]

print(f'\n{num_list} => {[i for i in num_list if num_list.count(i) == 1]}')