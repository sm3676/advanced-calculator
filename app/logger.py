import logging
import os


def setup_logger(log_file="calculator.log"):
    logger = logging.getLogger("CalculatorLogger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        os.makedirs("logs", exist_ok=True)

        file_handler = logging.FileHandler(f"logs/{log_file}")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger