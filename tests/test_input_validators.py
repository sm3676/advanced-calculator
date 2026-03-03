import pytest
from app.input_validators import validate_number
from app.exceptions import CalculatorError

def test_validate_number_success():
    assert validate_number("10", 100) == 10.0

def test_validate_number_invalid():
    with pytest.raises(CalculatorError):
        validate_number("abc", 100)

def test_validate_number_exceeds():
    with pytest.raises(CalculatorError):
        validate_number("500", 100)