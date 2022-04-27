"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


# Функция для красоты вывода
def refactor_text(ell):
    if ell < 100:
        ell_to_text = ' ' + str(ell)
    else:
        ell_to_text = ell
    return ell_to_text


def return_ascii(ell=32, result='', step=0):
    if ell == 128:
        return result
    else:
        if step == 10:
            result += '\n'
            step = -1
        else:
            result += f' | {refactor_text(ell)} - "{chr(ell)}"'
    return return_ascii(ell + 1, result, step + 1)


print(return_ascii())
