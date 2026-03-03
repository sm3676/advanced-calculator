from app.operations import OperationFactory
from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento
from app.history import LoggingObserver, AutoSaveObserver
from app.calculator_config import CalculatorConfig
from app.exceptions import (
    InvalidOperationError,
    MaxInputExceededError,
    UndoNotAvailableError,
    RedoNotAvailableError,
)


class Calculator:
    def __init__(self):
        self.history = []
        self.observers = []
        self.undo_stack = []
        self.redo_stack = []

        self.config = CalculatorConfig()   # Added config

        # register observers
        self.register_observer(LoggingObserver())
        self.register_observer(AutoSaveObserver())

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, calculation):
        for observer in self.observers:
            observer.update(calculation)

    def save_state(self):
        memento = CalculatorMemento(self.history.copy())
        self.undo_stack.append(memento)

    def undo(self):
        if not self.undo_stack:
            raise UndoNotAvailableError("No actions to undo")

        self.redo_stack.append(CalculatorMemento(self.history.copy()))
        memento = self.undo_stack.pop()
        self.history = memento.get_saved_state()

    def redo(self):
        if not self.redo_stack:
            raise RedoNotAvailableError("No actions to redo")

        self.undo_stack.append(CalculatorMemento(self.history.copy()))
        memento = self.redo_stack.pop()
        self.history = memento.get_saved_state()

    def perform_calculation(self, operation_name, a, b):

        # Enforce MAX_INPUT_VALUE
        if abs(a) > self.config.MAX_INPUT_VALUE or abs(b) > self.config.MAX_INPUT_VALUE:
            raise MaxInputExceededError(f"Input exceeds maximum allowed value of {self.config.MAX_INPUT_VALUE}")

        self.save_state()
        self.redo_stack.clear()

        try:
            operation = OperationFactory.get_operation(operation_name)
        except Exception:
            raise InvalidOperationError(f"Invalid operation: {operation_name}")
        
        result = operation.execute(a, b)

        #Apply Precision
        result = round(result, self.config.PRECISION)

        calculation = Calculation(operation_name, a, b, result)
        self.history.append(calculation)

        self.notify_observers(calculation)

        return result

    def get_history(self):
        return self.history

    def clear_history(self):
        self.save_state()
        self.history.clear()