class FixedArray:
    def __init__(self, size):
        self.data = [None] * size

    def set(self, index, value):
        if 0 <= index < len(self.data):
            self.data[index] = value
        else:
            raise IndexError("Индекс вышел за границы массива")

    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        raise IndexError("Индекс вышел за границы массива")