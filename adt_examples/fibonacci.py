class Fib:
    def __init__(self):
        self.prev = 1
        self.current = 2
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.prev > 10000:
            raise StopIteration
        result = self.prev
        self.prev, self.current = self.current, self.prev + self.current
        return result
