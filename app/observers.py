class Observer:
    def update(self, calculation):
        pass


class LoggingObserver(Observer):
    def update(self, calculation):
        print(f"Logged: {calculation.operation} "
              f"{calculation.operand1}, {calculation.operand2} = {calculation.result}")


class AutoSaveObserver(Observer):
    def __init__(self, calculator):
        self.calculator = calculator

    def update(self, calculation):
        from app.history import save_history
        save_history(self.calculator.history, "history.csv")