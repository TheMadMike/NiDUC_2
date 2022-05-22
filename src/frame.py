class Frame:
    number: int
    data: int
    size: int

    def __init__(self, number, data, size):
        self.number = number
        self.data = data
        self.size = size

    def __str__(self):
        return f"[{self.number}, {self.data}, {self.size}]"