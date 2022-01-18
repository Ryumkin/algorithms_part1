def pop(self):
    if self.stack:
        return self.stack.pop()
    else:
        return 'error'


def top(self):
    if self.stack:
        return self.stack[-1]
    else:
        return 'error'
