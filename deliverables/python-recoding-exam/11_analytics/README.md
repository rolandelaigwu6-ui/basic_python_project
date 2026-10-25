# Task 11 — Counting dictionaries, percentages and reconciliation

Marks: 5/100. Independent exercise.

## Required function
```python
def summarize(records):
    ...
```

## Examination question

Count records and return a summary dictionary. You may assume every record has a valid canonical category, status and priority.

Return **exactly** these seven keys:

| Key | Meaning |
|---|---|
| `total` | Number of records |
| `by_status` | Counts for open, in_progress and resolved |
| `by_priority` | Counts for critical, high, medium and low |
| `by_category` | Counts for Network, Hardware, Software and Other |
| `unresolved` | Number open plus number in progress |
| `resolved` | Number currently resolved |
| `resolution_percentage` | Resolved divided by total, multiplied by 100 |

Include every listed option in the grouping dictionaries, even when its count is zero. Each record contributes once to each grouping. Count its **current** status, not its history.

Example: for three records, one open and two resolved:

```python
# total == 3
# by_status == {"open": 1, "in_progress": 0, "resolved": 2}
# unresolved == 1
# resolved == 2
# resolution_percentage == 2 / 3 * 100
```

Do not round the percentage. With no records, all counts are zero and the percentage is `0.0`; do not divide by zero. Do not modify the input.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
