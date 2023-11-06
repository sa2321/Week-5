"""A simple Reverse Polish Notation (RPN) calculator."""

import math

class RPCalc:
    """A simple Reverse Polish Notation (RPN) calculator."""
    
    def __init__(self):
        """Initialize the RPN calculator with an empty stack."""
        self.stack = []

    def push(self, n):
        if isinstance(n, (int, float)):
            self.stack.append(n)
        elif n in ["+", "-", "*", "/", "sin", "cos"]:
            if n in ["+", "-", "*", "/"]:
                if len(self.stack) < 2:
                    raise ValueError("Insufficient operands for operator")
                b = self.stack.pop()
                a = self.stack.pop()
                if n == "+":
                    result = a + b
                elif n == "-":
                    result = a - b
                elif n == "*":
                    result = a * b
                elif n == "/":
                    if b == 0:
                        raise ValueError("Division by zero")
                    result = a / b
                self.stack.append(result)
            elif n == "sin":
                if not self.stack:
                    raise ValueError("Empty stack")
                a = self.stack.pop()
                result = math.sin(a)
                self.stack.append(result)
            elif n == "cos":
                if not self.stack:
                    raise ValueError("Empty stack")
                a = self.stack.pop()
                result = math.cos(a)
                self.stack.append(result)
        else:
            raise ValueError(f"Unrecognized operator: {n}")

    def pop(self):
        """Pop and return the top value from the stack."""
        if not self.stack:
            raise ValueError("Empty stack")
        return self.stack.pop()

    def peek(self):
        """Peek at the top value on the stack without removing it."""
        if not self.stack:
            raise ValueError("Empty stack")
        return self.stack[-1]

    def __len__(self):
        """Return the number of elements currently on the stack."""
        return len(self.stack)
