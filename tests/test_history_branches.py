import os
import pandas as pd
from app.history import load_history, history_file

def test_load_history_when_file_not_exists(tmp_path, monkeypatch):
    # Point history_file to temp location
    fake_file = tmp_path / "fake.csv"
    monkeypatch.setattr("app.history.history_file", fake_file)

    df = load_history()

    assert isinstance(df, pd.DataFrame)
    assert df.empty