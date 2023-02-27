# Очередь

# Хвост всегда указывает на первую свободную для записи ячейку,
# а голова — на элемент, добавленный в очередь раньше всех остальных

# *После удаления элемента голова продолжает указывать на элемент,
# # который находится в очереди дольше всех из оставшихся

# При превышении допустимого размера очереди нужно вывести «error».
# При вызове операций pop() или peek() для пустой очереди нужно вывести «None».


class Queue:
    def __init__(self, n):
        self.queue = [None for _ in range(n)]
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    # добавить в очередь
    def push(self, item):
        if self.size == self.max_n:
            print('error')
        else:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_n  # что дает этот остаток? - это дает цикличный сдвиг
            self.size += 1

    # просто вывести на печать
    def peek(self):
        if self.size == 0:
            print('None')
        else:
            print(self.queue[self.head])

    # удалить и вывести на печать
    def pop(self):
        if self.size == 0:
            print('None')
        else:
            print(self.queue[self.head])
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_n
            self.size -= 1

    def get_size(self):
        print(self.size)


if __name__ == '__main__':
    num_commands = int(input())  # количество команд
    max_queue_size = int(input())  # максимально допустимый размер очереди

    q = Queue(max_queue_size)

    for i in range(num_commands):
        s = input().split()
        if s[0] == 'push':
            q.push(s[1])
        elif s[0] == 'pop':
            q.pop()
        elif s[0] == 'peek':
            q.peek()
        elif s[0] == 'size':
            q.get_size()
