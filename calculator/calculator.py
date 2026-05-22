"""Calculator class providing a unified interface for arithmetic operations."""

from .operations import OPERATIONS, add, divide, multiply, subtract


class Calculator:
    """Stateless calculator supporting add, subtract, multiply, and divide."""

    def calculate(self, operation: str, a: float, b: float) -> float:
        """Execute a named arithmetic operation on two numbers.

        Args:
            operation: One of 'add', 'subtract', 'multiply', 'divide'.
            a: First operand.
            b: Second operand.

        Raises:
            KeyError: If operation is not supported.
            ValueError: If the operation is mathematically invalid (e.g. divide by zero).
        """
        if operation not in OPERATIONS:
            supported = ", ".join(OPERATIONS)
            raise KeyError(
                f"Unsupported operation '{operation}'. Choose from: {supported}."
            )
        return OPERATIONS[operation](a, b)

    def supported_operations(self) -> list[str]:
        """Return the list of supported operation names."""
        return list(OPERATIONS)

    def add(self, a: float, b: float) -> float:
        """Return the sum of a and b."""
        return add(a, b)

    def subtract(self, a: float, b: float) -> float:
        """Return a minus b."""
        return subtract(a, b)

    def multiply(self, a: float, b: float) -> float:
        """Return the product of a and b."""
        return multiply(a, b)

    def divide(self, a: float, b: float) -> float:
        """Return a divided by b.

        Raises:
            ValueError: If b is zero.
        """
        return divide(a, b)
