# Task 20 — unittest, debugging and regression evidence

Marks: 5/100. Independent exercise.

## Required function
```python
def transfer(balances, source, target, amount):
    ...
```

## Examination question

Investigate and fix the deliberately broken `transfer` function supplied in `solution.py`.

`balances` is a dictionary mapping account labels to built-in nonnegative integer balances. You may assume the existing data is valid.

A valid transfer requires:

- `source` and `target` are strings naming existing accounts.
- They name different accounts.
- `amount` is a built-in integer greater than zero, not a boolean or integer subclass.
- The source has enough money.

Wrong argument types raise `TypeError`. Invalid actions, such as an unknown account, transferring to the same account, nonpositive amount or insufficient funds, raise `ValueError`.

On success, subtract from the source, add to the target and return `None`. The total money must stay the same. On failure, leave every balance unchanged.

Example:

```python
balances = {"Ada": 20, "Ben": 5}
transfer(balances, "Ada", "Ben", 7)  # returns None
# balances is now {"Ada": 13, "Ben": 12}; total is still 25.
transfer(balances, "Ada", "Ben", 14) # raises ValueError
# balances must remain {"Ada": 13, "Ben": 12}.
```

Do the investigation in this order:

1. **Before fixing the code**, run it and record a real failure in `investigation.md`.
2. Record the initial data, expected result, actual result, cause and correction. Use genuine results from your run.
3. Fix the implementation without deleting assertions to hide failures.
4. Add **at least two original tests** in `test_candidate.py`, beyond the supplied tests.
5. Rerun the tests and keep evidence of the results.

The task requires both working code and an explanation of the bug.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
