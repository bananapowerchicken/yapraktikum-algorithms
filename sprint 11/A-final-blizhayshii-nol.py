# A - ближайший ноль, ID: 82282818
n = int(input())                        # длина улицы
data = list(map(int, input().split()))  # информация о домах

zeros = []  # индексы нулей
res = data

for i in range(n):
    if data[i] == 0:
        zeros.append(i)


num_zeros = len(zeros)
board_prev = -1
if num_zeros == 1:
    board_next = n-1
else:
    board_next = zeros[0] + (zeros[1] - zeros[0]) // 2

for i in range(num_zeros):
    prev = zeros[i] - 1
    next = zeros[i] + 1

    while prev > board_prev:
        res[prev] = res[prev + 1] + 1
        prev -= 1

    while next <= board_next:
        res[next] = res[next - 1] + 1
        next += 1

    if i == num_zeros-1:
        break

    board_prev = board_next

    if i + 2 < num_zeros:
        board_next = zeros[i+1] + (zeros[i+2] - zeros[i+1]) // 2
    else:
        board_next = n-1


print(" ".join(map(str, res)))
