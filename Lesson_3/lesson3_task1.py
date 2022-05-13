"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
result = [0] * 8

for i in range(2, 100):
    for ell in range(2, 10):
        if i % ell == 0:
            result[ell - 2] += 1

for i in range(2, 10):
    print(f'{i} - {result[i - 2]}')
