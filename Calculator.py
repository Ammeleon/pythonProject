# A simple calculator
class Calculator:
    # empty constructor
    def __init__(self):
        pass

    @staticmethod
    def typeError(x1, x2):
        if x1 and x2 not in [int, float]:
            raise TypeError("arguments must be integers or floats")

    @staticmethod
    def add(x1, x2):
        return x1 + x2

    @staticmethod
    def multiply(x1, x2):
        return x1 * x2

    @staticmethod
    def subtract(x1, x2):
        return x1 - x2

    @staticmethod
    def divide(x1, x2):
        if x2 == 0:
            raise ValueError("arguments cannot be zero")
        else:
            return x1 / x2

