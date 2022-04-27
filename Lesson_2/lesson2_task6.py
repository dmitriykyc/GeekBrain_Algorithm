"""
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться,
больше или меньше введенное пользователем число, чем то,
что загадано. Если за 10 попыток число не отгадано, вывести правильный ответ.
"""
from random import randint


def game(number, step=10):
    if step == 0:
        return f'Попытки закончились, загаданное число: {number}'

    else:
        user_numb = int(input('Введите Ваше число: '))
        if user_numb == numb:
            return f'Отлично! Верный ответ {number}'
        elif user_numb > numb:
            print(f'Загаданное число меньше чем {user_numb}, осталось {step - 1} попыток.')
        else:
            print(f'Загаданное число больше чем {user_numb}, осталось {step - 1} попыток.')

    return game(number, step - 1)


numb = randint(0, 101)
game_start = game(number=numb)
print(game_start)
