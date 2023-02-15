# A - ближайший ноль, ID: 82369737

def find_closest_zeros(n: int, data: list) -> list:
    res = [n for _ in range(n)]
    curr_zero_ind = -1

    for i in range(n):
        if data[i] == 0:
            curr_zero_ind = i
            res[i] = 0
        elif curr_zero_ind > -1:
            res[i] = res[i-1] + 1

    for i in range(n-1, -1, -1):
        if data[i] == 0:
            curr_zero_ind = i
        elif i < curr_zero_ind:
            if curr_zero_ind - i <= res[i-1] or i == 0:
                res[i] = res[i+1] + 1

    return res


if __name__ == '__main__':
    n = int(input())                        # длина улицы
    data = list(map(int, input().split()))  # информация о домах

    res = find_closest_zeros(n, data)
    print(*res)
