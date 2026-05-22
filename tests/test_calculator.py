import pytest

from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


# --- individual operation methods (backward-compatible API) ---

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0


def test_subtract(calc):
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(0, 5) == -5


def test_multiply(calc):
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-2, 5) == -10
    assert calc.multiply(0, 100) == 0


def test_divide(calc):
    assert calc.divide(10, 2) == 5
    assert calc.divide(7, 2) == 3.5


def test_divide_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(5, 0)


# --- calculate() dispatch ---

def test_calculate_dispatches_all_operations(calc):
    assert calc.calculate("add", 1, 2) == 3
    assert calc.calculate("subtract", 5, 3) == 2
    assert calc.calculate("multiply", 4, 5) == 20
    assert calc.calculate("divide", 10, 2) == 5


def test_calculate_raises_on_unknown_operation(calc):
    with pytest.raises(KeyError):
        calc.calculate("modulo", 10, 3)


def test_calculate_propagates_divide_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.calculate("divide", 9, 0)


# --- supported_operations ---

def test_supported_operations_returns_all_four(calc):
    assert set(calc.supported_operations()) == {"add", "subtract", "multiply", "divide"}
