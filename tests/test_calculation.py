import pytest
from app.calculation import Calculation


def test_calculation_creation():
    calc = Calculation(10, 5, "add", 15)

    assert calc.operand1 == 10
    assert calc.operand2 == 5
    assert calc.operation == "add"
    assert calc.result == 15


def test_calculation_str_representation():
    calc = Calculation(4, 2, "multiply", 8)

    result_str = str(calc)

    assert "multiply" in result_str
    assert "4" in result_str
    assert "2" in result_str
    assert "8" in result_str