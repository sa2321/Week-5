"""A module defining a Deque (double-ended queue) data structure."""


class Deque:
    """A class for implementing a Deque data structure."""

    def __init__(self, size):
        """Initialize class for implementing a Deque data structure."""
        self.size = size
        self.buffer = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0

    def append(self, x):
        """Add an element to the rear of the Deque."""
        if self.count == self.size:
            raise IndexError("Deque is full")
        self.buffer[self.rear] = x
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def appendleft(self, x):
        """Add an element to the front of the Deque."""
        if self.count == self.size:
            raise IndexError("Deque is full")
        self.front = (self.front - 1) % self.size
        self.buffer[self.front] = x
        self.count += 1

    def pop(self):
        """Remove and return an element from the rear of the Deque."""
        if self.count == 0:
            raise IndexError("Deque is empty")
        self.rear = (self.rear - 1) % self.size
        value = self.buffer[self.rear]
        self.buffer[self.rear] = None
        self.count -= 1
        return value

    def popleft(self):
        """Remove and return an element from the front of the Deque."""
        if self.count == 0:
            raise IndexError("Deque is empty")
        value = self.buffer[self.front]
        self.buffer[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return value

    def peek(self):
        """Return the element from the rear of the Deque."""
        if self.count == 0:
            raise IndexError("Deque is empty")
        return self.buffer[(self.rear - 1) % self.size]

    def peekleft(self):
        """Return the element from the front of the Deque."""
        if self.count == 0:
            raise IndexError("Deque is empty")
        return self.buffer[self.front]

    def __len__(self):
        """Return the current number of elements in the Deque."""
        return self.count

    def __iter__(self):
        """Iterate through the elements of the Deque."""
        current = self.front
        for _ in range(self.count):
            yield self.buffer[current]
            current = (current + 1) % self.size
