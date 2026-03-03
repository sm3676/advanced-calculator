import logging
import os
from app.calculator_config import CalculatorConfig

config = CalculatorConfig()

if not os.path.exists(config.LOG_DIR):
    os.makedirs(config.LOG_DIR)

log_file = os.path.join(config.LOG_DIR, "calculator.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def get_logger():
    return logging.getLogger()