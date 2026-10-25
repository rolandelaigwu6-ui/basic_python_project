# Task 12 — Whole-collection validation and uniqueness scopes

Marks: 5/100. Independent exercise.

## Required function
```python
def validate_batches(records):
    ...
```

## Examination question

Check a whole list of records and their notes. Return `None` when everything is valid. Do not change anything.

Each record must be a dictionary containing:

- `id`: a nonblank string with no whitespace at either end.
- `notes`: a list of dictionaries.

Each note dictionary must contain:

- `note_id`: a nonblank string with no whitespace at either end.
- `message`: a nonblank string with no whitespace at either end.

Extra fields are allowed in records and notes.

There are two different duplicate rules:

1. Record IDs must be unique across the whole list.
2. Note IDs must be unique **inside each record**. Different records may reuse a note ID.

Example:

```python
records = [
    {"id": "alpha", "notes": [{"note_id": "first", "message": "Check cable"}]},
    {"id": "beta", "notes": [{"note_id": "first", "message": "Check power"}]},
]
validate_batches(records)  # returns None: reusing "first" across records is allowed
```

Two `"first"` notes inside `alpha` would be invalid. Two records with ID `"alpha"` would also be invalid.

Wrong container or field types raise `TypeError`. Missing fields, duplicates or invalid strings raise `ValueError`. Reject surrounding whitespace instead of trimming it. IDs here are arbitrary strings: do **not** enforce the R001/N001 format from earlier tasks.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
