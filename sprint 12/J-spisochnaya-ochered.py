# Любимый вариант очереди Тимофея — очередь, написанная с использованием
# связного списка. Помогите ему с реализацией. Очередь должна поддерживать
# выполнение трёх команд:

# get() — вывести элемент, находящийся в голове очереди, и удалить его.
# Если очередь пуста, то вывести «error».
# put(x) — добавить число x в очередь
# size() — вывести текущий размер очереди

# В первой строке записано количество команд n — целое число,
# не превосходящее 1000. В каждой из следующих n строк записаны команды по
# одной строке.

class ListQueue:
    def __init__(self):
        self.queue = []
        self.head = 0
        self.size = 0

    def get(self):
        if self.size:
            print(self.queue[self.head])
            self.queue.pop(self.head)
            self.size -= 1
        else:
            print('error')

    def put(self, item):
        self.queue.append(item)
        self.size += 1

    def get_size(self):
        return self.size


if __name__ == '__main__':
    num_commands = int(input())  # количество команд    

    q = ListQueue()

    for i in range(num_commands):
        s = input().split()
        if s[0] == 'get':
            q.get()
        elif s[0] == 'put':
            q.put(s[1])
        elif s[0] == 'size':
            print(q.get_size())
