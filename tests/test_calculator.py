import pytest
from app.calculator import Calculator


def test_calculator_add():
    calc = Calculator()
    result = calc.calculate("add", 5, 3)

    assert result == 8


def test_calculator_history():
    calc = Calculator()

    calc.calculate("add", 1, 2)
    calc.calculate("multiply", 2, 3)

    history = calc.get_history()

    assert len(history) == 2


def test_calculator_undo():
    calc = Calculator()

    calc.calculate("add", 1, 2)
    calc.calculate("multiply", 2, 3)

    calc.undo()
    history = calc.get_history()

    assert len(history) == 1


def test_calculator_redo():
    calc = Calculator()

    calc.calculate("add", 1, 2)
    calc.calculate("multiply", 2, 3)

    calc.undo()
    calc.redo()

    history = calc.get_history()

    assert len(history) == 2


def test_calculator_clear_history():
    calc = Calculator()

    calc.calculate("add", 1, 2)
    calc.clear_history()

    history = calc.get_history()

    assert len(history) == 0