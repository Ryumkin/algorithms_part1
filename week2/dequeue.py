class Queue:

    def __init__(self, max_len=100):
        self.max_len = max_len + 1
        self.queue = [0] * self.max_len
        self.head = 0
        self.tail = 0

    def empty(self):
        return self.head == self.tail

    def enqueue(self, key):
        self.queue[self.tail] = key
        self.tail = (self.tail + 1) % self.max_len

    def dequeue(self):
        if self.empty():
            return "error"
        res = self.queue[self.head]
        self.head = (self.head + 1) % self.max_len
        return res


t = Queue()
t.enqueue(1)
t.dequeue()
print(t.dequeue())
