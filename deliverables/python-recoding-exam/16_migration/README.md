# Task 16 — Compatibility, copying and explicit repair boundaries

Marks: 5/100. Independent exercise.

## Required function
```python
def upgrade_records(records):
    ...
```

## Examination question

Upgrade older records by adding a missing `notes` field. Return a deep copy and never change the original data.

The input must be a list of dictionaries. Every record must contain `id`, which must be a unique, nonblank string with no whitespace at either end.

Handle `notes` this way:

- If the key is absent, add `"notes": []` to the copied record.
- If the key exists, its value must be a list of strings. Preserve those strings exactly.
- An existing `"notes": None` is invalid. It does not mean the field is missing.

Preserve all extra fields, including nested data, in the deep copy.

Example:

```python
original = [
    {"id": "A", "label": "Old record"},
    {"id": "B", "notes": ["  Keep this spacing  "]},
]
upgraded = upgrade_records(original)
# upgraded[0] now has notes=[]; original[0] still has no notes key.
# upgraded[1]["notes"] is ["  Keep this spacing  "] unchanged.
```

Wrong input, record, ID, notes-list or note-item types raise `TypeError`. Missing IDs, blank/untrimmed IDs or duplicate IDs raise `ValueError`.

Even if a later record fails validation, no earlier source record may have been changed. Editing nested data in the returned result must not affect the source.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
