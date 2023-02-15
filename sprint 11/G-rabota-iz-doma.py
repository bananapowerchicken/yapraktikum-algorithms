# Вася реализовал функцию, которая переводит целое число из десятичной системы
# в двоичную. Но, кажется, она получилась не очень оптимальной.

# Попробуйте написать более эффективную программу.

# Не используйте встроенные средства языка по переводу чисел в бинарное
# представление.

# # A - наивный - деление до упора - 131ms 4.24Mb

# res = []
# current = int(input())
# if current == 0:
#     print(0)
# else:
#     while current >= 1:
#         res.append(current % 2)
#         current = current//2


#     print("".join(map(str, res[::-1])))


# B - побитовый - дб быстрее - 107ms 4.22Mb - даааа))
mask = int(input())
res = []

if mask == 0:
    print(0)
else:
    curr = 1
    i = 0

    while 1:
        if pow(2, i) > mask:
            break
        res.append((curr & mask) >> i)
        i += 1
        curr = curr << 1    

    print("".join(map(str, res[::-1])))