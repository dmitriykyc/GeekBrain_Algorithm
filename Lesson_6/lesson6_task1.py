"""Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa") -> 6
func("sova") -> 9
"""
import hashlib


def get_str(str_us):
    result_str = set()

    for i in range(len(str_us)):
        for j in range(len(str_us) - 1 if i == 0 else len(str_us), i, -1):
            str_new = bytes(str_us[i:j].encode('utf-8'))
            result_str.add(hashlib.sha1(str_new).hexdigest())

    return result_str


str_user = str(input("Введите строку: "))

print("Количество различных подстрок в этой строке:", len(get_str(str_user)))
