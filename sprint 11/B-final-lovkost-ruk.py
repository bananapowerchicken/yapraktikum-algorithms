# B - ловкость рук, ID: 82420893
ROWS_AMOUNT = 4


def count_points(s, k):
    num_amount = {}
    finger_limit = k * 2
    res = 0

    for i in s:
        if i != '.':
            if i not in num_amount:
                num_amount[i] = 0
            num_amount[i] += 1

    for val in num_amount.values():
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
