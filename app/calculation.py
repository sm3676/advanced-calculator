from datetime import datetime


class Calculation:
    def __init__(self, operation, operand1, operand2, result):
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = result
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.timestamp} | {self.operation} | {self.operand1}, {self.operand2} = {self.result}"