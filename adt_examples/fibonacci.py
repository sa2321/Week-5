"""A module defines a Fibonacci number generator."""

class Fib:
    """A class for generating Fibonacci numbers using an iterator."""

    def __init__(self):
    """Define the first two terms of the the sequence."""
        self.prev = 1
        self.current = 2

    def __iter__(self):
        """Return the iterator object."""
        return self

    def __next__(self):
        """Generate the next Fibonacci number."""
        if self.prev > 10000:
            raise StopIteration
        result = self.prev
        self.prev, self.current = self.current, self.prev + self.current
        return result
