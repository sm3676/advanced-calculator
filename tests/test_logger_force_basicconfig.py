import importlib
import app.logger

def test_logger_basicconfig_executes():
    importlib.reload(app.logger)
    logger = app.logger.get_logger()
    assert logger is not None