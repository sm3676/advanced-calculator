import os
import pandas as pd
from app.calculator_config import CalculatorConfig

config = CalculatorConfig()

# Create history directory if not exists
if not os.path.exists(config.HISTORY_DIR):
    os.makedirs(config.HISTORY_DIR)

history_file = os.path.join(config.HISTORY_DIR, "history.csv")


def save_history(operation, operand1, operand2, result):
    new_entry = {
        "Operation": operation,
        "Operand1": operand1,
        "Operand2": operand2,
        "Result": result
    }

    # If file exists, append
    if os.path.exists(history_file):
        df = pd.read_csv(history_file)
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)

        # Enforce MAX_HISTORY_SIZE
        if len(df) > config.MAX_HISTORY_SIZE:
            df = df.tail(config.MAX_HISTORY_SIZE)
    else:
        df = pd.DataFrame([new_entry])

    df.to_csv(history_file, index=False)


def load_history():
    if os.path.exists(history_file):
        return pd.read_csv(history_file)
    return pd.DataFrame()