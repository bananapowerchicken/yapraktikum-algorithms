# Нужно реализовать класс StackMax, который поддерживает операцию определения
# максимума среди всех элементов в стеке. Класс должен поддерживать операции
# push(x), где x – целое число, pop() и get_max().

class StackMax:

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

    def get_max(self):
        '''' Поиск максимального эл-та стека '''
        if len(self.items) == 0:
            return ('None')
        return max(self.items)


if __name__ == '__main__':
    curr_stack = StackMax()
    n = int(input())  # кол-во команд
    res = []

    while n > 0:
        command_arg = input().split()

        if command_arg[0] == 'push':
            curr_stack.push(int(command_arg[1]))
        elif command_arg[0] == 'pop':
            if curr_stack.pop() == 'error':
                res.append('error')
        elif command_arg[0] == 'get_max':
            res.append(curr_stack.get_max())

        n -= 1

    print('\n'.join([str(item) for item in res]))
