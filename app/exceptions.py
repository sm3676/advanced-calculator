class CalculatorError(Exception):
    """Base class for calculator exceptions"""
    pass


class InvalidOperationError(CalculatorError):
    """Raised when invalid operation is requested"""
    pass


class MaxInputExceededError(CalculatorError):
    """Raised when input exceeds max allowed value"""
    pass


class UndoNotAvailableError(CalculatorError):
    """Raised when undo is not possible"""
    pass


class RedoNotAvailableError(CalculatorError):
    """Raised when redo is not possible"""
    pass