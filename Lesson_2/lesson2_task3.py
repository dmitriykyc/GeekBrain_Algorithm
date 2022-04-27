"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""


def result(numb, new_str=''):
    if not numb:
        return new_str
    else:
        last_numb = numb % 10
        if new_str == '' and last_numb == 0:
            pass
        else:
            new_str += str(last_numb)
    return result(numb // 10, new_str)


numbers = int(input('Введите число: '))
res = result(numbers)
print(res)

