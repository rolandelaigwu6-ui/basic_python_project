# Task 13 — JSON syntax versus business validity

Marks: 5/100. Independent exercise.

## Required function
```python
def decode_catalog(text):
    ...
```

## Examination question

Turn JSON text into a validated list of catalog records. This task receives text; it does not read a file.

1. If `text` is not a string, raise `TypeError`.
2. Decode the JSON.
3. Check that the result is a list of dictionaries.
4. Check every record using the rules below.
5. Return the decoded records if everything is valid.

Each record needs:

| Field | Rule |
|---|---|
| `id` | Nonblank string, already trimmed, unique across records |
| `name` | Nonblank string, already trimmed |
| `quantity` | Built-in integer of 0 or more; not a boolean |

Extra keys are allowed. Do not fix or trim invalid data.

Examples:

```python
decode_catalog('[{"id": "P1", "name": "Pen", "quantity": 2}]')
# returns [{"id": "P1", "name": "Pen", "quantity": 2}]
decode_catalog('[]')              # returns []
decode_catalog('{broken JSON')    # raises ValueError
decode_catalog('{"id": "P1"}')    # raises ValueError: top level is not a list
decode_catalog(123)               # raises TypeError: input is not text
```

After the initial text type check, **all invalid content raises `ValueError`**: JSON syntax errors, wrong structure, missing fields, wrong decoded field types, invalid values or duplicate record IDs.

Also reject duplicate JSON member names at **any depth**, including inside extra fields. For example, an object containing `"quantity": 1, "quantity": 2` is invalid; do not silently keep one value. Successfully decoding JSON does not prove the data follows these rules.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
