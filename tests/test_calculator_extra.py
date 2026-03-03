import pytest
from app.calculator import Calculator
from app.exceptions import InvalidOperationError

def test_invalid_operation():
    calc = Calculator()

    with pytest.raises(InvalidOperationError):
        calc.calculate("invalid", 1, 2)