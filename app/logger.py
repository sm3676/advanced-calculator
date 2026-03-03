import logging
import os
from app.calculator_config import CalculatorConfig


# Load configuration
config = CalculatorConfig()


# Ensure log directory exists
if not os.path.exists(config.LOG_DIR):
    os.makedirs(config.LOG_DIR)


# Define log file path
log_file = os.path.join(config.LOG_DIR, "calculator.log")


# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def get_logger():
    """Return configured logger instance"""
    return logging.getLogger("calculator")