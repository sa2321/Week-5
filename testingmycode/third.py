from adt_examples.deque import Deque

# Create an instance of the deque with a fixed size
deque = Deque(5)

# Example usage
deque.append(1)
deque.append(2)
deque.append(3)
print(list(deque))  # Should print [1, 2, 3]

