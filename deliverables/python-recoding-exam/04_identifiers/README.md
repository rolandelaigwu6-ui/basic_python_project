# Task 04 — Parsing, ASCII digits and numeric ordering

Marks: 5/100. Independent exercise.

## Required function
```python
def next_code(codes):
    ...
```

## Examination question

Given a list of IDs, check that they are valid, then return the ID after the largest number.

For example, `['R002', 'R010', 'R005']` contains the numbers 2, 10 and 5. The largest is 10, so the next ID is `"R011"`. The list does not need to be sorted.

Rules for each ID:

- It must be a string starting with uppercase `R`.
- After `R`, use only ordinary ASCII digits `0`–`9`.
- The number must be greater than zero.
- Write the number with at least three digits, adding only the zeros needed to reach three digits.
- Do not allow whitespace or repeated IDs.

| Number | Correct ID | Incorrecfor i in range(1,10):
    print(f"R{i  + 1 :03d}")t example |
|---|---|---|
| 1 | `R001` | `R1` or `R0001` |
| 10 | `R010` | `R10` |
| 999 | `R999` | `R0999` |
| 1000 | `R1000` | `R01000` |

Examples:

```python
next_code(["R010", "R002", "R099"])  # returns "R100"
next_code(["R999"])                 # returns "R1000"
next_code([])                       # returns "R001"
next_code(["R001", "R001"])         # raises ValueError: duplicate
next_code(["R000"])                 # raises ValueError: zero
next_code(["R００１"])              # raises ValueError: Unicode digits
next_code([1])                      # raises TypeError: item is not a string
next_code("R001")                   # raises TypeError: input is not a list
```

Wrong container or item types raise `TypeError`. Invalid spelling or duplicates raise `ValueError`. Do not change the input list.

To understand the parts: `"R010"` is the whole ID, `"010"` is its numeric text, and `10` is its numeric value. Compare numeric values when finding the largest ID.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices. b

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
