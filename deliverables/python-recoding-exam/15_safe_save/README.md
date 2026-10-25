# Task 15 — JSON writing, temporary files and cleanup

Marks: 5/100. Independent exercise.

## Required function
```python
def save_snapshot(records, path):
    ...
```

## Examination question

Save a list of dictionaries as a complete UTF-8 JSON file, protecting an existing destination if the save fails.

Check that `records` is a list and each entry is a dictionary. Wrong types raise `TypeError`. No particular business fields are required, but the contents must be JSON-serializable. Reject `NaN` and positive/negative infinity with `ValueError` instead of writing nonstandard JSON.

Use this save sequence:

1. Validate the input.
2. Write the complete JSON to a temporary file **in the destination directory**.
3. Close the temporary file.
4. Replace the destination by calling `os.replace(temp_path, path)`.

Import `os` and call `os.replace` in that form so the supplied test can simulate replacement failure.

Example:

```python
save_snapshot([{"id": "P1", "quantity": 2}], path)
# The destination contains JSON representing this list.
save_snapshot([], path)
# The destination contains JSON representing an empty list.
```

If validation, JSON encoding or replacement fails, preserve any existing destination and remove temporary files created by the failed attempt. Return `None` on success. Do not change `records`. The parent directory already exists, and `path` is a string or `pathlib.Path`. JSON whitespace/layout does not matter.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
