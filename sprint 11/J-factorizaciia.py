# Основная теорема арифметики говорит: любое число раскладывается на 
# произведение простых множителей единственным образом, с точностью до их
# перестановки. Например:

# Число 8 можно представить как 2 × 2 × 2.
# Число 50 –— как 2 × 5 × 5 (или 5 × 5 × 2, или 5 × 2 × 5). Три варианта
# отличаются лишь порядком следования множителей.
# Разложение числа на простые множители называется факторизацией числа.

# Напишите программу, которая производит факторизацию переданного числа.
MIN_NUM = 2


def factorizate(n):
    res = [1]
    max_num = n
    curr_num = MIN_NUM

    while res[-1] <= max_num:
        z, r = divmod(max_num, curr_num)
        if not r:
            max_num = z
            res.append(curr_num)
            curr_num = MIN_NUM

        else:
            curr_num += 1

    return res[1::]


if __name__ == '__main__':
    n = int(input())
    res = factorizate(n)

    print(*res)