"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
(индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
"""

import random

numbers = [random.randint(0, 100) for i in range(20)]
print(numbers)
result = []
for item, ell in enumerate(numbers):
    if ell % 2 == 0:
        result.append(item)

print(result)
