import os
import pytest
from app.calculator_config import CalculatorConfig


def test_invalid_max_history_size(monkeypatch):
    monkeypatch.setenv("CALCULATOR_MAX_HISTORY_SIZE", "0")
    with pytest.raises(ValueError):
        CalculatorConfig()


def test_invalid_precision(monkeypatch):
    monkeypatch.setenv("CALCULATOR_PRECISION", "-1")
    with pytest.raises(ValueError):
        CalculatorConfig()


def test_invalid_max_input(monkeypatch):
    monkeypatch.setenv("CALCULATOR_MAX_INPUT_VALUE", "0")
    with pytest.raises(ValueError):
        CalculatorConfig()