from app.operations import OperationFactory
from app.calculation import Calculation


class Calculator:
    def __init__(self):
        self.history = []
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, calculation):
        for observer in self.observers:
            observer.update(calculation)

    def perform_calculation(self, operation_name, a, b):
        operation = OperationFactory.get_operation(operation_name)
        result = operation.execute(a, b)

        calculation = Calculation(operation_name, a, b, result)
        self.history.append(calculation)

        self.notify_observers(calculation)

        return result

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history.clear()