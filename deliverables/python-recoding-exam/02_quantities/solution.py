"""Candidate implementation. Follow README.md; no solution is provided."""

def validate_quantity(value):
    if type(value) is not int:
        raise TypeError("Quantity must be a built-in integera")

    if value >= 1 and value <= 500:
        return value
    raise ValueError("qauntity must be between 1 and 500")