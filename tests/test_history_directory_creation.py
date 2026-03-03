import importlib
import shutil
import os
import app.history

def test_history_directory_creation(tmp_path, monkeypatch):
    fake_dir = tmp_path / "new_history"

    # Force env before reload
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(fake_dir))

    # Remove directory if exists
    if os.path.exists(fake_dir):
        shutil.rmtree(fake_dir)

    # Reload module to trigger directory creation
    importlib.reload(app.history)

    assert os.path.exists(fake_dir)