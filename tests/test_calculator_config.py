from app.calculator_config import CalculatorConfig

def test_config_all_attributes():
    config = CalculatorConfig()

    # Force access of everything
    attributes = vars(config)

    for key, value in attributes.items():
        assert value is not None