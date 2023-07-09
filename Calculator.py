# A simple calculator
class Calculator:
    # empty constructor
    def __init__(self):
        pass

    def typeError(self, x1, x2):
        if x1 and x2 not in [int, float]:
            raise TypeError("arguments must be integers or floats")

    def add(self, x1, x2):
        return x1 + x2

    def multiply(self, x1, x2):
        return x1 * x2

    def subtract(self, x1, x2):
        return x1 - x2

    def divide(self, x1, x2):
        if x2 == 0:
            raise ValueError("arguments cannot be zero")
        else:
            return x1 / x2

