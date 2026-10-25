# Task 10 — Sorting keys and regression preservation

Marks: 5/100. Independent exercise.

## Required function
```python
def open_queue(records):
    ...
```

## Examination question

Build a queue containing only records whose status is exactly `"open"`. You may assume the records are valid and have canonical `T` IDs, status and priority.

Sort the returned queue by these two rules:

1. Priority first: `critical`, then `high`, then `medium`, then `low`.
2. Within the same priority, sort by the numeric part of the ID, smallest first.

Example, showing just status, priority and ID:

```text
Input:
T010  open         high
T002  open         high
T001  resolved     critical
T020  open         critical
T003  in_progress  low

Returned order:
T020  critical
T002  high
T010  high
```

Compare ID numbers numerically: 999 comes before 1000, even though text sorting can give a different result.

Return detached deep copies, including nested extra fields. Leave the input list's order and all its data unchanged. Do not include in-progress or resolved records.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
