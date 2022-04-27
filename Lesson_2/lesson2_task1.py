"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю
о невозможности деления на ноль, если он ввел его в качестве делителя.
"""
import operator


def result(num_operator):
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    return f'Результат: {num_operator(a, b)}'


while True:
    method = input('Введите знак операции ("+", "-", "*", "/"), для выхода наберите - "0": ')

    if method == '0':
        print('Вы ввели 0 и остановили программу.')
        break
    elif method == '+':
        print(result(operator.add))
        continue
    elif method == '-':
        print(result(operator.sub))
        continue
    elif method == '*':
        print(result(operator.mul))
        continue
    elif method == '/':
        try:
            print(result(operator.truediv))
        except ZeroDivisionError:
            print('На ноль не делим')
            print(result(operator.truediv))
        continue
    else:
        print("Вы ввели не верный оператор")