# Реализуйте класс StackMaxEffective, поддерживающий операцию определения
# максимума среди элементов в стеке. Сложность операции должна быть O(1). Для
# пустого стека операция должна возвращать None. При этом push(x) и pop() также
# должны выполняться за константное время.

# по сути и правда даже сами значения не нужны, только максимум и длина стека,
# то есть можно использовать чисто стек максимумов

# тут вот любопытный натыренный и пока непрозрачный момент структуры максимум
# + значение - по технике, идея как раз ясна, а второй массив неохота


class StackMaxEffective:

    def __init__(self):
        self.max_stack = []

    def push(self, elem):
        ''' Добавление эл-та в стек '''
        if self.max_stack:
            self.max_stack.append((elem, max(elem, self.max_stack[-1][1])))
        else:
            self.max_stack.append((elem, elem))

    def pop(self):
        ''' Удаление и вывод эл-та из стека'''
        if not self.max_stack:
            return ('error')
        return self.max_stack.pop()

    def get_max(self):
        '''' Поиск максимального эл-та стека '''
        if not self.max_stack:
            return ('None')
        return (self.max_stack[-1][1])


if __name__ == '__main__':
    curr_stack = StackMaxEffective()
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
