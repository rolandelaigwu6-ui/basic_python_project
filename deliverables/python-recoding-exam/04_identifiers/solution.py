"""Candidate implementation. Follow README.md; no solution is provided."""

def next_code(codes):
    if not isinstance(codes, list):
        raise TypeError("code must be a list")
    seen = set()
    highest = 0

    for code in codes:
        if not isinstance(code, str):
            raise TypeError("Each ID must be a string")
        if not code.startswith("R"):
            raise ValueError("ID must start with R")
        digits = code[1:]

        if not (digits.isascii() and digits.isdigit()):
            raise ValueError("must contain only ASCII digits")

        val = int(digits)
        if val <= 0:
            raise ValueError("must be a positive integer")

        if f"R{val:03d}" != code:
            raise ValueError("Invalid digit padding or formatting")

        if code in seen:
            raise ValueError("Duplicate ID")
        seen.add(code)

        if val > highest:
            highest = val
    return f"R{highest + 1:03d}"



print(next_code(["R010", "R002", "R099"]))  # returns "R100"
print(next_code(["R999"]))                 # returns "R1000"
#next_code([])                       # returns "R001"
print(next_code(["R001", "R002"]))         # raises ValueError: duplicate
print(next_code(["R002"]))                 # raises ValueError: zero
print(next_code(["R001"]))              # raises ValueError: Unicode digits
#next_code([1])                      # raises TypeError: item is not a string
print(next_code(["R001"]))    