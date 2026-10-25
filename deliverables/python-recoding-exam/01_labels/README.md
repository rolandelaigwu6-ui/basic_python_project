# Task 01 — Strings, whitespace and Unicode

Marks: 5/100. Independent exercise.

## Required function
```python
def normalize_label(value):
    ...
```

## Examination question

Create a function that cleans a reader's label and returns the cleaned text.

1. The input must be a string. Otherwise, raise `TypeError`.
2. Remove whitespace from the beginning and end.
3. Replace each group of whitespace inside the label with one ordinary space. Whitespace includes spaces, tabs and newlines.
4. Use casefolding to make the text consistent regardless of letter case. Casefolding also handles Unicode characters such as `ß`.
5. If the cleaned label is empty, raise `ValueError`.

Examples:

```python
normalize_label("  Hello   Club  ")  # returns "hello club"
normalize_label("  STRAẞE   Club ")  # returns "strasse club"
normalize_label("Hello\tClub")      # returns "hello club"
normalize_label("   ")              # raises ValueError
normalize_label(123)                # raises TypeError
```

Return the result. Do not print anything or ask the user for input.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
