class Deque:

    def __init__(self):
        self.deque = []

    def push_front(self, key):
        self.deque.insert(0, key)
        return "ok"

    def push_back(self, key):
        self.deque.append(key)
        return "ok"

    def pop_front(self):
        if self.empty():
            return "error"
        return self.deque.pop(0)

    def pop_back(self):
        if self.empty():
            return "error"
        return self.deque.pop()

    def front(self):
        if self.empty():
            return "error"
        return self.deque[0]

    def back(self):
        if self.empty():
            return "error"
        return self.deque[-1]

    def clear(self):
        self.deque.clear()
        return "ok"

    def size(self):
        return len(self.deque)

    def empty(self):
        return self.size() == 0


def process_deque(commands: list):
    deque = Deque()
    result = []
    for command in commands:
        args = command.split()
        if len(args) == 2:
            if args[0] == 'push_front':
                result.append(deque.push_front(int(args[1])))
            elif args[0] == 'push_back':
                result.append(deque.push_back(int(args[1])))
        else:
            if args[0] == 'pop_front':
                result.append(deque.pop_front())
            elif args[0] == 'pop_back':
                result.append(deque.pop_back())
            elif args[0] == 'front':
                result.append(deque.front())
            elif args[0] == 'back':
                result.append(deque.back())
            elif args[0] == 'clear':
                result.append(deque.clear())
            elif args[0] == 'size':
                result.append(deque.size())
    return result


if __name__ == "__main__":
    test_cmd = ["push_front 1", "push_front 2", "push_back 6", "front", "back", "clear", "size", "back"]
    # should print ["ok", "ok", "ok", 2, 6, "ok", 0, "error"]
    print(process_deque(test_cmd))

    test_cmd = ["pop_front", "back", "push_back 2", "size"]
    # should print ["error", "error", "ok", 1]
    print(process_deque(test_cmd))

    test_cmd = ["push_back 1", "push_front 10", "push_front 4", "push_front 5", "back", "pop_back", "pop_back", "back"]
    # should print ["ok", "ok", "ok", "ok", 1, 1, 10, 4]
    print(process_deque(test_cmd))
