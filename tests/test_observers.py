from app.observers import LoggingObserver

class DummyCalculation:
    operation = "multiply"
    operand1 = 3
    operand2 = 4
    result = 12

def test_logging_observer_update(capsys):
    observer = LoggingObserver()
    calc = DummyCalculation()

    observer.update(calc)

    captured = capsys.readouterr()
    assert "multiply" in captured.out
    assert "3" in captured.out
    assert "4" in captured.out
    assert "12" in captured.out