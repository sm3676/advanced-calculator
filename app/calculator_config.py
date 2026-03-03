import os
from dotenv import load_dotenv


class CalculatorConfig:
    def __init__(self):
        load_dotenv()

        self.LOG_DIR = os.getenv("CALCULATOR_LOG_DIR", "logs")
        self.HISTORY_DIR = os.getenv("CALCULATOR_HISTORY_DIR", "history")
        self.MAX_HISTORY_SIZE = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", 100))
        self.AUTO_SAVE = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"
        self.PRECISION = int(os.getenv("CALCULATOR_PRECISION", 2))
        self.MAX_INPUT_VALUE = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", 1000000))
        self.DEFAULT_ENCODING = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")

        self.validate_config()

    def validate_config(self):
        if self.MAX_HISTORY_SIZE <= 0:
            raise ValueError("MAX_HISTORY_SIZE must be greater than 0")

        if self.PRECISION < 0:
            raise ValueError("PRECISION cannot be negative")

        if self.MAX_INPUT_VALUE <= 0:
            raise ValueError("MAX_INPUT_VALUE must be greater than 0")
  