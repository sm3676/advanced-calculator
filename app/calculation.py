from datetime import datetime


class Calculation:
    def __init__(self, operand1, operand2, operation, result):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operation = operation
        self.result = result
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.operation} {self.operand1}, {self.operand2} = {self.result}"