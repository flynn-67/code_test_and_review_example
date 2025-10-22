def add(a, b):
    """Add two numbers."""
    return a + b

def minus(a, b):
    """Subtract b from a."""
    return a - b

def divide(a, b):
    """Divide a by b safely."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
