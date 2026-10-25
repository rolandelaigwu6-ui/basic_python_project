# Task 06 — Validate before mutation and exceptions

Marks: 5/100. Independent exercise.

## Required function
```python
def reserve_stock(items, code, amount):
    ...
```

## Examination question

Reserve a quantity from an existing stock entry.

`items` is a dictionary whose keys are item codes. Each value is a dictionary containing `stock` and possibly extra fields. You may assume its existing contents are valid.

1. Check the argument types: `items` must be a dictionary, `code` a string and `amount` a built-in integer. Reject booleans and integer subclasses for `amount`. Wrong types raise `TypeError`.
2. Check that the code exists, the amount is greater than zero and enough stock is available. Otherwise, raise `ValueError`.
3. Only after all checks succeed, subtract the amount from that item's stock.
4. Return its remaining stock.

Example:

```python
items = {"P1": {"stock": 8, "label": "Pens"}}
reserve_stock(items, "P1", 3)  # returns 5
# items is now {"P1": {"stock": 5, "label": "Pens"}}
reserve_stock(items, "P1", 6)  # raises ValueError; stock stays 5
reserve_stock(items, "P2", 1)  # raises ValueError; unknown code
```

On any failure, leave the entire collection unchanged, including nested data. Preserve extra fields. Do not add or delete entries.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
