# Task 02 — Types, booleans and integer boundaries

Marks: 5/100. Independent exercise.

## Required function
```python
def validate_quantity(value):
    ...
```

## Examination question

Check whether the input is an ordinary Python integer between **1 and 500, including both endpoints**.

- Accept only the built-in `int` type. Reject booleans, floats, strings and subclasses of `int` with `TypeError`.
- If it is a built-in integer but is below 1 or above 500, raise `ValueError`.
- If it is valid, return the same value unchanged.
- Do not convert other types into integers.

Examples:

```python
validate_quantity(1)      # returns 1
validate_quantity(250)    # returns 250
validate_quantity(500)    # returns 500
validate_quantity(0)      # raises ValueError
validate_quantity(501)    # raises ValueError
validate_quantity("10")   # raises TypeError, even though it looks numeric
validate_quantity(10.0)   # raises TypeError
validate_quantity(True)   # raises TypeError
```

Think of two separate questions: “Is it the required type?” and then “Is its value in the allowed range?”

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
