import pytest
from app.calculator import Calculator
from app.exceptions import UndoNotAvailableError, RedoNotAvailableError


def test_undo_empty():
    calc = Calculator()
    with pytest.raises(UndoNotAvailableError):
        calc.undo()


def test_redo_empty():
    calc = Calculator()
    with pytest.raises(RedoNotAvailableError):
        calc.redo()


def test_clear_and_get_history():
    calc = Calculator()
    calc.calculate("add", 1, 1)
    calc.clear_history()
    assert calc.get_history() == []