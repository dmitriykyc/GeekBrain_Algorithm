"""
Определить, какое число в массиве встречается чаще всего.
"""
import random

numbers = [random.randint(0, 4) for i in range(20)]
result = {}

for ell in set(numbers):
    result[ell] = 0

for i in numbers:
    result[i] += 1

max_numm = {'num': 0, 'eqq': 0}

for i in result:
    if result[i] > max_numm['eqq']:
        max_numm['num'] = str(i)
        max_numm['eqq'] = result[i]

print(numbers)
print(result)
print(f'Число {max_numm["num"]} встречается чаще всего, а именно {max_numm["eqq"]} раз. ')
