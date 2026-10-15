class Deque:
    def __init__(self):
        self.items = []

    def append_left(self, item):
        self.items.insert(0, item)

    def append_right(self, item):
        self.items.append(item)

    def pop_left(self):
        return self.items.pop(0) if self.items else None

    def pop_right(self):
        return self.items.pop() if self.items else None