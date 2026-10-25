# Task 18 — Separation of data and logic; exact scoring

Marks: 5/100. Independent exercise.

## Required function
```python
def score_answers(bank, answers):
    ...
```

## Examination question

Count how many submitted answers match the question bank.

`bank` must be a list of dictionaries. Every question needs:

- `id`: a unique, nonblank string.
- `correct`: a string containing exactly `"A"`, `"B"`, `"C"` or `"D"`.

`answers` must be a list of the same length, with each item exactly `"A"`, `"B"`, `"C"` or `"D"`. Compare by position: the first answer belongs to the first question, and so on.

Example:

```python
bank = [{"id": "q1", "correct": "B"}, {"id": "q2", "correct": "D"}]
score_answers(bank, ["B", "A"])  # returns 1
score_answers(bank, ["B", "D"])  # returns 2
score_answers([], [])            # returns 0
score_answers(bank, ["b", "D"])  # raises ValueError: lowercase is not accepted
```

Wrong top-level, item or field types raise `TypeError`. Missing keys, duplicate/blank IDs, invalid choices or mismatched lengths raise `ValueError`.

Do not trim or uppercase submitted answers. Do not change either input. Always use the `correct` values supplied in the bank; questions can be reordered, so do not hardcode an answer key.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
