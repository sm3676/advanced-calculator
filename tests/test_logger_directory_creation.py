import importlib
import shutil
import os
import app.logger

def test_logger_directory_creation(tmp_path, monkeypatch):
    fake_dir = tmp_path / "new_logs"

    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(fake_dir))

    if os.path.exists(fake_dir):
        shutil.rmtree(fake_dir)

    importlib.reload(app.logger)

    assert os.path.exists(fake_dir)