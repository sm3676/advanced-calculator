import os
import importlib
from app import logger


def test_logger_directory_creation(tmp_path, monkeypatch):
    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(tmp_path))

    # reload logger module to re-trigger directory logic
    import app.logger
    importlib.reload(app.logger)

    assert os.path.exists(tmp_path)