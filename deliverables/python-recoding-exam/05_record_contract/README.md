# Task 05 — Dictionaries, required keys and invariants

Marks: 5/100. Independent exercise.

## Required function
```python
def validate_device(record):
    ...
```

## Examination question

Check that a device dictionary follows these rules. Return `None` if it is valid.

The dictionary must contain all four keys below. Extra keys are allowed and must be left alone.

| Key | Required value |
|---|---|
| `serial` | A nonempty string with no whitespace at either end |
| `label` | A nonempty string with no whitespace at either end |
| `stock` | A built-in integer of 0 or more; not a boolean or integer subclass |
| `state` | A string containing exactly `"available"` or `"retired"` |

There is one additional rule: **a retired device must have stock 0**. An available device may also have stock 0.

Examples:

```python
validate_device({"serial": "D1", "label": "Printer", "stock": 3, "state": "available"})
# returns None
validate_device({"serial": "D1", "label": "Printer", "stock": 0, "state": "retired"})
# returns None
validate_device({"serial": "D1", "label": "Printer", "stock": 3, "state": "retired"})
# raises ValueError: retired devices cannot have stock
```

Wrong dictionary or field types raise `TypeError`. Missing keys or invalid values raise `ValueError`. For example, `stock=True` is a type error; `stock=-1` is a value error. Reject `" Printer "` rather than trimming it. Never change the dictionary.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
