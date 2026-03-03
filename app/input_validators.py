from app.exceptions import CalculatorError, MaxInputExceededError


def validate_number(value, max_value):
    try:
        number = float(value)
    except ValueError:
        raise CalculatorError("Input must be numeric")

    if abs(number) > max_value:
        raise MaxInputExceededError("Input exceeds maximum allowed value")

    return number