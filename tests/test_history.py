from app.history import save_history, load_history

def test_history_full_coverage(tmp_path, monkeypatch):
    monkeypatch.setattr("app.history.config.HISTORY_DIR", tmp_path)
    monkeypatch.setattr("app.history.history_file", tmp_path / "history.csv")
    monkeypatch.setattr("app.history.config.MAX_HISTORY_SIZE", 1)

    # First save
    save_history("add", 1, 1, 2)

    # Second save triggers trimming branch
    save_history("subtract", 5, 3, 2)

    df = load_history()

    assert len(df) == 1