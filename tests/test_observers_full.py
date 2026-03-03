import pytest
from app.observers import Observer, AutoSaveObserver
from app.calculator import Calculator


def test_base_observer_update():
    obs = Observer()
    # should simply execute pass
    obs.update(None)


def test_autosave_observer(monkeypatch):
    calc = Calculator()
    observer = AutoSaveObserver(calc)

    # monkeypatch save_history to avoid real file call
    called = {}

    def fake_save_history(history, filename):
        called["yes"] = True

    monkeypatch.setattr("app.history.save_history", fake_save_history)

    observer.update(None)

    assert "yes" in called