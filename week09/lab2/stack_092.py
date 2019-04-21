class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, arg):
        self.l.append(arg)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def __len__(self):
        return len(self.l)

    def is_empty(self):
        return len(self) == 0
