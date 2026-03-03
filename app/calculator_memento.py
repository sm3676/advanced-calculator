class CalculatorMemento:
    def __init__(self, history_state):
        # store a copy of history
        self._history_state = history_state.copy()

    def get_saved_state(self):
        return self._history_state