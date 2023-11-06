from adt_examples.rpcalc import RPCalc

# Create an instance of the calculator
calculator = RPCalc()

# Example usage
calculator.push(5)
calculator.push(3)
calculator.push("+")
result = calculator.pop()
print(result)  # Should print 8.0
