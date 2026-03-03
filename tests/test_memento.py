from app.calculator_memento import CalculatorMemento

def test_memento_stores_state():
    state = [1, 2, 3]
    m = CalculatorMemento(state)

    assert m.get_saved_state() == state