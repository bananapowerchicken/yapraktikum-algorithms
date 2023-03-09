# A - Дек, ID: 83660838

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
            raise ValueError('Deque is full')        
        self.buff[self.head - 1] = item
        self.head = (self.head - 1) % self.max_n
        self.size += 1

    def push_back(self, item):
        if self.size == self.max_n:
            raise ValueError('Deque is full')
        self.buff[self.tail] = item
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError

        res = self.buff[self.head]

        self.buff[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1

        return res

    def pop_back(self):
        if self.is_empty():
            raise IndexError

        res = self.buff[self.tail-1]

        self.buff[self.tail-1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1

        return res


if __name__ == '__main__':
    num_commands = int(input())  # количество команд
    max_buff_size = int(input())  # максимально допустимый размер буфера

    d = Deque(max_buff_size)

    for _ in range(num_commands):
        command = input()
        operation, *val = command.split()

        try:
            res = getattr(d, operation)(*val)
            if res is not None:
                print(res)
        except ValueError:
            print('error')
        except IndexError:
            print('error')
