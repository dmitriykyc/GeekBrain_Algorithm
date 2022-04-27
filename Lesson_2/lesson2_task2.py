"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def result(numbers, even=0, odd=0):
    if not numbers:
        return f'Чётные: {even} \nНечётные: {odd}'
    elif numbers % 10 % 2 == 0:
        even += 1
    else:
        odd += 1
    return result(numbers // 10, even, odd)


numbers = int(input('Введите число: '))
res = result(numbers)
print(res)
