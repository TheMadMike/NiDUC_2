class Frame:
    number: int
    size: int
    data: int
    checksum: int = 0

    def __init__(self, number, data, size):
        self.number = number
        self.data = data
        self.size = size

    def copy(self):
        return Frame(self.number, self.data, self.size)

    def __str__(self):
        return f"[{self.number}, {self.data}, {self.size}]"