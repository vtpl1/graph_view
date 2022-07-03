from . import main


def create_app(test_config=None):
    return main.create_app(test_config=test_config)