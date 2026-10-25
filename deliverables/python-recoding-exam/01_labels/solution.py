"""Candidate implementation. Follow README.md; no solution is provided."""

def normalize_label(value):

    if not isinstance(value, str):
        raise TypeError("value must be of a datatype string")
    
    valuee = " ".join(value.strip().split())
    if not valuee:
        raise ValueError("value must not be empty")
    return valuee.casefold()

