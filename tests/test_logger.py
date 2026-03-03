import os
from app.logger import get_logger
from app.calculator_config import CalculatorConfig

def test_logger_creation(tmp_path, monkeypatch):
    # Redirect LOG_DIR
    monkeypatch.setattr("app.logger.config.LOG_DIR", tmp_path)

    logger = get_logger()

    assert logger is not None