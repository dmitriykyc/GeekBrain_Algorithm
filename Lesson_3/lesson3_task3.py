"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

numbers = [random.randint(0, 100) for i in range(20)]
print(numbers)
min_num = {"num": 101, 'pos': 0}
max_num = {"num": 0, 'pos': 0}

for pos, ell in enumerate(numbers):
    if ell < min_num['num']:
        min_num['num'] = ell
        min_num['pos'] = pos
    if ell > max_num['num']:
        max_num['num'] = ell
        max_num['pos'] = pos

numbers[min_num['pos']], numbers[max_num['pos']] = numbers[max_num['pos']], numbers[min_num['pos']]
print(numbers)
