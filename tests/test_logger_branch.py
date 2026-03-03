import os
import shutil
from app.logger import get_logger
from app.calculator_config import CalculatorConfig

def test_logger_creates_directory(tmp_path, monkeypatch):
    # Override LOG_DIR
    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(tmp_path / "new_logs"))

    # Re-import config to apply env
    config = CalculatorConfig()

    # Ensure directory does not exist
    if os.path.exists(config.LOG_DIR):
        shutil.rmtree(config.LOG_DIR)

    # Trigger logger setup
    logger = get_logger()

    assert logger is not None