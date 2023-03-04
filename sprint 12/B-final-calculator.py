# B - Калькулятор, ID: 83358943

def calculate(s):
    operands = []
    operators = '+-/*'
    for item in s:
        if item not in operators:
            operands.append(int(item))
            res = item
        else:
            if item == '+':
                res = operands[-2] + operands[-1]   
            if item == '-':
                res = operands[-2] - operands[-1]
            if item == '*':
                res = operands[-2] * operands[-1]                
            if item == '/':
                res = operands[-2] // operands[-1]            
            operands.pop()
            operands.pop()
            operands.append(res)

    print(res)


if __name__ == '__main__':
    s = input().split()
    calculate(s)
