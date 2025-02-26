from src.main import Calculator
#from . import
def test_init():

    red = Calculator()

    assert red.add(1, 2) == 3