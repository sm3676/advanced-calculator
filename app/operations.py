import math


class Add:
    def execute(self, a, b):
        return a + b


class Subtract:
    def execute(self, a, b):
        return a - b


class Multiply:
    def execute(self, a, b):
        return a * b


class Divide:
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


class Power:
    def execute(self, a, b):
        return a ** b


class Modulus:
    def execute(self, a, b):
        return a % b


class IntDivide:
    def execute(self, a, b):
        return a // b


class Percent:
    def execute(self, a, b):
        return (a / b) * 100


class AbsDiff:
    def execute(self, a, b):
        return abs(a - b)


class Root:
    def execute(self, a, b):
        return math.pow(a, 1 / b)


class OperationFactory:

    @staticmethod
    def create(operation_name):

        operations = {
            "add": Add(),
            "subtract": Subtract(),
            "multiply": Multiply(),
            "divide": Divide(),
            "power": Power(),
            "modulus": Modulus(),
            "int_divide": IntDivide(),
            "percent": Percent(),
            "abs_diff": AbsDiff(),
            "root": Root()
        }

        if operation_name not in operations:
            raise ValueError("Invalid operation")

        return operations[operation_name]