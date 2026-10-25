# Task 03 — Condition precedence and pure functions

Marks: 5/100. Independent exercise.

## Required function
```python
def dispatch_level(severity, people):
    ...
```

## Examination question

Choose an emergency drill level using the severity and the number of people.

First validate the inputs:

- `severity` must be a string containing exactly `"low"`, `"medium"` or `"high"`. Do not trim it or change its case.
- `people` must be a built-in integer greater than zero. Booleans and integer subclasses are not accepted.
- Wrong types raise `TypeError`. Other invalid values raise `ValueError`.

Then apply these rules **in this order**, returning the first matching level:

| Condition | Return |
|---|---|
| Severity is high **and** people is at least 10 | `"critical"` |
| Otherwise, severity is high **or** people is at least 10 | `"high"` |
| Otherwise, severity is medium **or** people is at least 3 | `"medium"` |
| Otherwise | `"low"` |

“At least 10” includes 10; “at least 3” includes 3.

Examples:

```python
dispatch_level("high", 10)  # "critical"
dispatch_level("high", 2)   # "high"
dispatch_level("low", 10)   # "high"
dispatch_level("low", 3)    # "medium"
dispatch_level("low", 2)    # "low"
dispatch_level("HIGH", 2)   # raises ValueError
dispatch_level("low", 0)    # raises ValueError
```

Do not print anything or read input.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
