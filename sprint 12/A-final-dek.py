# A - Дек, ID: 83201002

class Deque:
    def __init__(self, n):
        self.buff = [None for _ in range(n)]
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_front(self, item):
        if self.size == self.max_n:
            raise OverflowError
        else:
            self.buff[self.head - 1] = item
            self.head = (self.head - 1) % self.max_n
            self.size += 1

    def push_back(self, item):
        if self.size == self.max_n:
            raise OverflowError
        else:
            self.buff[self.tail] = item
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        else:
            print(self.buff[self.head])
            self.buff[self.head] = None
            self.head = (self.head + 1) % self.max_n
            self.size -= 1

    def pop_back(self):
        if self.is_empty():
            raise IndexError
        else:
            print(self.buff[self.tail-1])
            self.buff[self.tail-1] = None
            self.tail = (self.tail - 1) % self.max_n
            self.size -= 1


if __name__ == '__main__':
    num_commands = int(input())  # количество команд
    max_buff_size = int(input())  # максимально допустимый размер буфера

    d = Deque(max_buff_size)

    commands_dict = {
        'push_front': d.push_front,
        'push_back': d.push_back,
        'pop_front': d.pop_front,
        'pop_back': d.pop_back,
    }

    for _ in range(num_commands):
        command = input()
        operation, *val = command.split()
        if val:
            try:
                res = commands_dict[operation](int(*val))
                if res is not None:
                    print(res)
            except OverflowError:
                print('error')
        else:
            try:
                res = commands_dict[operation]()
                if res is not None:
                    print(res)
            except IndexError:
                print('error')
