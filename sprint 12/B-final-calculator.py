# B - Калькулятор, ID: 83358943
import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


def calculate(s):
    operands = []

    for item in s:
        if item not in operators:
            operands.append(int(item))
            res = item
        else:
            res = operators[item](operands[-2], operands[-1])
            operands.pop()
            operands.pop()
            operands.append(res)

    print(res)


if __name__ == '__main__':
    s = input().split()
    calculate(s)
