from abc import ABC, abstractmethod
import math


class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class AddOperation(Operation):
    def execute(self, a, b):
        return a + b


class SubtractOperation(Operation):
    def execute(self, a, b):
        return a - b


class MultiplyOperation(Operation):
    def execute(self, a, b):
        return a * b


class DivideOperation(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class PowerOperation(Operation):
    def execute(self, a, b):
        return a ** b


class RootOperation(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Root degree cannot be zero")
        return a ** (1 / b)


class ModulusOperation(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot modulus by zero")
        return a % b


class IntegerDivisionOperation(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a // b


class PercentageOperation(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot calculate percentage with zero")
        return (a / b) * 100


class AbsoluteDifferenceOperation(Operation):
    def execute(self, a, b):
        return abs(a - b)


class OperationFactory:

    @staticmethod
    def get_operation(operation_name):
        operations = {
            "add": AddOperation(),
            "subtract": SubtractOperation(),
            "multiply": MultiplyOperation(),
            "divide": DivideOperation(),
            "power": PowerOperation(),
            "root": RootOperation(),
            "modulus": ModulusOperation(),
            "int_divide": IntegerDivisionOperation(),
            "percent": PercentageOperation(),
            "abs_diff": AbsoluteDifferenceOperation(),
        }

        if operation_name not in operations:
            raise ValueError(f"Invalid operation: {operation_name}")

        return operations[operation_name]