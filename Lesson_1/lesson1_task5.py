"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

letters = 'abcdefghijklmnopqrstuvwxyz'
letter1 = str(input('Введите первую букву: '))
letter2 = str(input('Введите вторую букву: '))
position_letter1 = letter.index(letter1) + 1
position_letter2 = letter.index(letter2) + 1
len_letters = position_letter2 - position_letter1 - 1

print(f'Буква "{letter1}" занимает {position_letter1}ю позицию в алфавите\n'
      f'Буква "{letter2}" занимает {position_letter2}ю позицию в алфавите\n'
      f'Между этими буквами {len_letters} букв')