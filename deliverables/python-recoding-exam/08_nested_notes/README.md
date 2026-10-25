# Task 08 — Nested lists, validation, ID continuity and aliasing

Marks: 5/100. Independent exercise.

## Required function
```python
def append_note(record, author, message):
    ...
```

## Examination question

Add one note to a record, then return a separate copy of the new note.

You may assume `record` is a valid dictionary with `status` and `notes`. Existing notes have unique valid IDs, authors and messages.

Before adding anything:

- Allow notes only when status is `"open"` or `"in_progress"`.
- Require `author` and `message` to be strings. Wrong types raise `TypeError`.
- Trim whitespace from both ends of the author and message.
- The trimmed author must not be blank.
- The trimmed message must have **5 to 300 characters, including both endpoints**.
- Invalid content or status raises `ValueError`.

Give the new note an ID one greater than the highest existing numeric note ID. Use `N001` when there are no notes. Follow Task 04's formatting rule, but use `N` instead of `R`. Find the largest number; do not assume the last note has the largest ID.

Example:

```python
record = {"status": "open", "notes": []}
append_note(record, "  Ada  ", "  Check cable  ")
# Appends and returns {"note_id": "N001", "author": "Ada", "message": "Check cable"}
```

If existing note IDs are `N002` and `N010`, the next is `N011`.

Append the note to the original record, but return a detached deep copy: editing the returned note must not edit the stored note. If anything fails, change nothing and do not consume an ID.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
