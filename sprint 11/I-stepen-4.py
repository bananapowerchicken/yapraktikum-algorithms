# Напишите программу, которая определяет, будет ли положительное целое число
# степенью четвёрки.

# Подсказка: степенью четвёрки будут все числа вида 4n, где n – целое
# неотрицательное число.

# Формат ввода
# На вход подаётся целое число в диапазоне от 1 до 10000.

# Формат вывода
# Выведите «True», если число является степенью четырёх, «False» –— в обратном
# случае.

MAX_INPUT = 10000


def count_pow_four(n):
    res = 'False'
    pows_of_four = [1]

    while pows_of_four[-1] * 4 < MAX_INPUT:
        pows_of_four.append(pows_of_four[-1] * 4)

    if n in pows_of_four:
        res = 'True'

    return res


if __name__ == '__main__':
    n = int(input())
    res = count_pow_four(n)

    print(*res)
