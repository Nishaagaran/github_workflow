"""Pure arithmetic operation functions used by the Calculator class."""

from typing import Callable


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


OPERATIONS: dict[str, Callable[[float, float], float]] = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}
