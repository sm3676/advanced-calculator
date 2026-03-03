from app.operations import OperationFactory
from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento


class Calculator:
    def __init__(self):
        self.history = []
        self.observers = []
        self.undo_stack = []
        self.redo_stack = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, calculation):
        for observer in self.observers:
            observer.update(calculation)

    def save_state(self):
        memento = CalculatorMemento(self.history)
        self.undo_stack.append(memento)

    def undo(self):
        if not self.undo_stack:
            raise Exception("No actions to undo")

        self.redo_stack.append(CalculatorMemento(self.history))
        memento = self.undo_stack.pop()
        self.history = memento.get_saved_state()

    def redo(self):
        if not self.redo_stack:
            raise Exception("No actions to redo")

        self.undo_stack.append(CalculatorMemento(self.history))
        memento = self.redo_stack.pop()
        self.history = memento.get_saved_state()

    def perform_calculation(self, operation_name, a, b):
        self.save_state()
        self.redo_stack.clear()

        operation = OperationFactory.get_operation(operation_name)
        result = operation.execute(a, b)

        calculation = Calculation(operation_name, a, b, result)
        self.history.append(calculation)

        self.notify_observers(calculation)

        return result

    def get_history(self):
        return self.history

    def clear_history(self):
        self.save_state()
        self.history.clear()