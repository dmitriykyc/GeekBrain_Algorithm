"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа. Например,
пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import defaultdict, deque


def my_translate(value_str, table):
    numbers = deque(value_str)
    numbers.reverse()
    result = 0
    for i in range(len(numbers)):
        result += table[numbers[i]] * 16 ** i
    return result


def my_operation(numb, table):
    resul_operation = deque()
    while numb > 0:
        d = numb % 16
        for i in table_int:
            if table[i] == d:
                resul_operation.append(i)
        numb //= 16
    resul_operation.reverse()
    return list(resul_operation)


value_int = '0123456789ABCDEF'
table_int = defaultdict(int)
num = 0
for ell in value_int:
    table_int[ell] += num
    num += 1

first_num = my_translate(input('Введите 1 число в шестнадцатеричном формате: '), table_int)
second_num = my_translate(input('Введите 2 число в шестнадцатеричном формате: '), table_int)

print(f'Сумма двух чисел: {my_operation(first_num + second_num, table_int)}')
print(f'Произведение двух чисел: {my_operation(first_num * second_num, table_int)}')
