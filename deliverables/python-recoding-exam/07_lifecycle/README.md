# Task 07 — State machines and guarded assignment

Marks: 5/100. Independent exercise.

## Required function
```python
def apply_action(records, record_id, action, staff=None):
    ...
```

## Examination question

Perform one action on an existing record. `records` is a valid list of dictionaries with `id`, `status`, `assigned_to` and `notes`. IDs are unique strings. You may assume the stored data is valid.

Find the record whose `id` equals `record_id`. An unknown ID raises `ValueError`. `record_id` and `action` must be strings; wrong types raise `TypeError`.

Use these action rules:

| Action | When allowed | Change |
|---|---|---|
| `"assign"` | Record is open or in progress | Store the trimmed staff label in `assigned_to` |
| `"start"` | Record is open and already assigned | Set status to `"in_progress"` |
| `"resolve"` | Record is in progress | Set status to `"resolved"` |
| `"reopen"` | Record is resolved | Set status to `"open"` |

For assignment, `staff` must be a string with nonblank content after trimming. Wrong staff type raises `TypeError`; blank staff raises `ValueError`. Do not assign a resolved record. The staff requirement applies to the assign action.

Unknown actions and actions that are not allowed in the current state raise `ValueError`.

Example sequence for an initially open, unassigned record `T001`:

```python
apply_action(records, "T001", "assign", "  Ada  ")  # stores "Ada"
apply_action(records, "T001", "start")             # status becomes in_progress
apply_action(records, "T001", "resolve")           # status becomes resolved
apply_action(records, "T001", "reopen")            # status becomes open
```

Update the original record on success and return a **deep copy** of that updated record. A deep copy means changing the returned record, including its nested notes, cannot change the stored record. Status changes must preserve assignment and notes. On any rejected action, leave the whole collection unchanged.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
