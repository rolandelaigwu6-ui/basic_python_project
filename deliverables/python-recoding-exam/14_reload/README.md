# Task 14 — File reading, exceptions and transactional replacement

Marks: 5/100. Independent exercise.

## Required function
```python
def reload_catalog(current, path):
    ...
```

## Examination question

Load a catalog file into an existing list, replacing the list's contents only if the whole load succeeds.

- Read `path` as UTF-8 text.
- Validate the text using the exact catalog rules from Task 13.
- Use this folder's supplied `decoder.py`. Do not edit it or import another exercise's implementation.
- Once reading and validation have both succeeded, replace the contents of `current`.
- Return `None`.

The original list object must stay the same object. Any other variable referring to that list must see the new contents too.

Example:

```python
current = [{"id": "old", "name": "Old item", "quantity": 1}]
other_reference = current
# Suppose the file contains: [{"id": "new", "name": "New item", "quantity": 2}]
reload_catalog(current, path)
# current now contains the new record.
# other_reference sees that same new record.
# current is other_reference remains True.
```

File failures must propagate as `OSError` (including subclasses such as `FileNotFoundError`). Invalid content raises `ValueError`. In either case, leave the old in-memory contents untouched. Do not modify any file.

A file containing the JSON text `[]` successfully clears the list. A missing file must not clear it. A completely empty file is invalid JSON; it is different from `[]`.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
