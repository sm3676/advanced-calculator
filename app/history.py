import pandas as pd
import os
from app.logger import setup_logger


class Observer:
    def update(self, calculation):
        pass


class LoggingObserver(Observer):
    def __init__(self):
        self.logger = setup_logger()

    def update(self, calculation):
        self.logger.info(
            f"{calculation.operation} | "
            f"{calculation.operand1}, {calculation.operand2} "
            f"= {calculation.result}"
        )


class AutoSaveObserver(Observer):
    def __init__(self, file_path="history/calculation_history.csv"):
        self.file_path = file_path
        os.makedirs("history", exist_ok=True)

    def update(self, calculation):
        data = [{
            "operation": calculation.operation,
            "operand1": calculation.operand1,
            "operand2": calculation.operand2,
            "result": calculation.result,
            "timestamp": calculation.timestamp,
        }]

        df = pd.DataFrame(data)

        if os.path.exists(self.file_path):
            df.to_csv(self.file_path, mode="a", header=False, index=False)
        else:
            df.to_csv(self.file_path, index=False)