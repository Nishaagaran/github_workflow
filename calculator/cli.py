"""Command-line interface for the calculator application."""

from .calculator import Calculator


def _prompt_float(label: str) -> float | None:
    """Prompt the user for a float value, returning None on invalid input."""
    try:
        return float(input(f"{label}: "))
    except ValueError:
        return None


def run() -> None:
    """Start the interactive calculator session."""
    calc = Calculator()
    ops = calc.supported_operations()

    print("Simple Calculator")
    print("-----------------")

    while True:
        print(f"\nOperations: {', '.join(ops)}, quit")
        op = input("Enter operation: ").strip().lower()

        if op == "quit":
            break

        if op not in ops:
            print(f"Invalid operation. Choose from: {', '.join(ops)}.")
            continue

        a = _prompt_float("First number")
        if a is None:
            print("Invalid number.")
            continue

        b = _prompt_float("Second number")
        if b is None:
            print("Invalid number.")
            continue

        try:
            result = calc.calculate(op, a, b)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
