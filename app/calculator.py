from app.operations import OperationFactory
from app.calculation import Calculation
from app.logger import get_logger
from app.input_validators import validate_number
from app.calculator_config import CalculatorConfig
from app.exceptions import (
    InvalidOperationError,
    UndoNotAvailableError,
    RedoNotAvailableError,
)


class Calculator:

    def __init__(self):
        self.history = []
        self._redo_stack = []
        self.logger = get_logger()
        self.config = CalculatorConfig()

    def calculate(self, operation, a, b):

        # Validate inputs using config max value
        a = validate_number(a, self.config.MAX_INPUT_VALUE)
        b = validate_number(b, self.config.MAX_INPUT_VALUE)

        try:
            op = OperationFactory.create(operation)
        except ValueError:
            raise InvalidOperationError("Invalid operation requested")

        result = op.execute(a, b)

        calculation = Calculation(a, b, operation, result)

        self.history.append(calculation)
        self._redo_stack.clear()

        self.logger.info(str(calculation))

        return result

    def undo(self):
        if not self.history:
            raise UndoNotAvailableError("Nothing to undo")

        calc = self.history.pop()
        self._redo_stack.append(calc)
        return calc

    def redo(self):
        if not self._redo_stack:
            raise RedoNotAvailableError("Nothing to redo")

        calc = self._redo_stack.pop()
        self.history.append(calc)
        return calc

    def clear_history(self):
        self.history.clear()
        self._redo_stack.clear()

    def get_history(self):
        return self.history