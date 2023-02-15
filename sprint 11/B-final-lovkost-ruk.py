# B - ловкость рук, ID: 82383934
ROWS_AMOUNT = 4


def count_points(s, k):
    dict = {}
    finger_limit = k * 2
    res = 0

    for i in s:
        if i != '.':
            if i not in dict:
                dict.update({i: 1})
            else:
                dict[i] += 1

    for val in dict.values():
        if val <= finger_limit:
            res += 1

    return res


if __name__ == '__main__':
    k = int(input())

    s = []
    for i in range(ROWS_AMOUNT):
        s += input().split()
    s = ''.join(s)

    res = count_points(s, k)
    print(res)
