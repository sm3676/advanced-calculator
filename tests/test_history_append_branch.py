import os
import pandas as pd
from app.history import save_history, load_history
from app.calculator_config import CalculatorConfig

def test_save_history_append(tmp_path, monkeypatch):
    # Redirect history_file
    fake_file = tmp_path / "history.csv"
    monkeypatch.setattr("app.history.history_file", fake_file)

    # First write (creates file)
    save_history("add", 1, 2, 3)

    # Second write (should append)
    save_history("sub", 5, 3, 2)

    df = load_history()

    assert len(df) == 2
    assert df.iloc[1]["Result"] == 2