import random

"""
Написать программу, которая генерирует в указанных пользователем границах:
● случайное целое число,
● случайное вещественное число,
● случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

which_test = int(input('Наберите: \n'
                       '1 - чтобы получить случайное целое число\n'
                       '2 - чтобы получить cлучайное вещественное число \n'
                       '3 - чтобы получить случайный символ\n'
                       'Ваш выбор: '))

if which_test == 1:
    print('Я выведу случайное целое число!')
    start_num = int(input('Введите стартовое число: '))
    finish_num = int(input('Введите конечное число: '))
    random_num = random.randint(start_num, finish_num)
    print(f'Результат: {random_num}')
elif which_test == 2:
    print('Я выведу случайное вещественное число!')
    start_num = float(input('Введите стартовое число: '))
    finish_num = float(input('Введите конечное число: '))
    random_num = random.uniform(start_num, finish_num)
    print(f'Результат: {random_num}')
elif which_test == 3:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    print('Я выведу случайную букву из диапазона!')
    start_letter = letters.index(input('Введите стартовую букву: '))
    finish_letter = letters.index(input('Введите конечную букву: '))
    result_letter = letters[random.randint(start_letter, finish_letter)]
    print(f'Случайная буква из диапазона: {result_letter}')
else:
    print('Вы обещали быть идеальным человеком, но всё пошло не по плану, запустите ещё разок')
