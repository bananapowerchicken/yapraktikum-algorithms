# B - Калькулятор, ID: 83722382
import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


class Stack_custom:
    def __init__(self):
        self.items = []

    def push(self, elem):
        ''' Добавление эл-та в стек '''
        self.items.append(elem)

    def pop(self):
        ''' Удаление и вывод эл-та из стека'''
        if len(self.items) == 0:
            return ('error')
        return self.items.pop()


def calculate(s):
    operands = Stack_custom()

    for item in s:
        if item not in OPERATORS:
            operands.push(int(item))
            res = item
        else:
            operand1 = operands.pop()
            operand2 = operands.pop()
            res = OPERATORS[item](operand2, operand1)
            operands.push(res)

    print(res)


if __name__ == '__main__':
    s = input().split()
    calculate(s)
