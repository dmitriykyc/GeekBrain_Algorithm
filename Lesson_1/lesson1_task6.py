"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

letters = 'abcdefghijklmnopqrstuvwxyz'
letter = str(input('Введите букву: '))
print(f'Позиция буквы в алфавите: {letters.index(letter) + 1}')