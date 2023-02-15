# B - ловкость рук, ID: 82281010

ROWS_AMOUNT = 4

k = int(input())
finger_limit = k * 2
res = 0

s = ""

for i in range(ROWS_AMOUNT):
    s += input()

s = s.replace('.', '')
if s != '':
    curr_symb = max(s)
    i = int(curr_symb)

    while i >= 0:
        curr_amount = s.count(curr_symb)
        if curr_amount > 0:
            if finger_limit >= curr_amount:
                res += 1
        i -= 1
        curr_symb = str(i)

print(res)
