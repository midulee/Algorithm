class Stack:
    def __init__(self, initial = None):
        if initial:
            self.member = initial
        else:
            self.member = []

    def push(self, new):
        self.member.append(new)

    def pop(self):
        self.member.pop()

    def top(self):
        print(self.member[-1])

    def empty(self):
        if self.member:
            return True
        return False

    def size(self):
        return len(self.member)

    def print(self):
        print(" ".join(map(str, self.member)))


