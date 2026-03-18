from pybliometrics import init
from pybliometrics.utils.startup import get_config

def initialize_pybliometrics():
    """
    Initialize pybliometrics if not already initialized.
    """
    try:
        get_config()
    except FileNotFoundError:
        init()
