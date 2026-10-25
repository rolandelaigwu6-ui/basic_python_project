# Task 09 — Comprehensions, casefold, AND filters and copies

Marks: 5/100. Independent exercise.

## Required function
```python
def find_records(records, text="", category="", status="", priority=""):
    ...
```

## Examination question

Return the records that match **every filter the caller supplied**. You may assume the stored ticket dictionaries are valid.

All four filter arguments must be strings. Otherwise, raise `TypeError`. Trim the filters and casefold them before matching. A blank or whitespace-only filter means “do not restrict this field.”

| Filter | Matching rule |
|---|---|
| `text` | Must appear somewhere inside the casefolded title |
| `category` | One of Network, Hardware, Software, Other, ignoring case |
| `status` | One of open, in_progress, resolved, ignoring case |
| `priority` | One of critical, high, medium, low, ignoring case |

An unknown nonblank category, status or priority raises `ValueError`, even if `records` is empty.

Example: suppose you have these records, along with any other valid fields:

```python
# Title             Category    Status    Priority
# "Printer issue"   Hardware    open      high
# "Printer setup"   Software    open      low
# "Cable issue"     Hardware    resolved  high
find_records(records, text=" PRINTER ", category=" hardware ", status="OPEN")
# Returns only the "Printer issue" record.
```

All supplied filters must match together: use AND behavior. Do not remove punctuation or use approximate/fuzzy matching.

Return deep copies of matching records in their original order. Changing a returned record or its nested data must not affect the input. Never change the inputs.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
