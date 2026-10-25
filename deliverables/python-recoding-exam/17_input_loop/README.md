# Task 17 — I/O injection, loops and termination

Marks: 5/100. Independent exercise.

## Required function
```python
def read_answer(prompt, input_fn=input, output_fn=print):
    ...
```

## Examination question

Ask for an answer until the user enters A, B, C or D, then return that answer.

- Read using `input_fn(prompt)`.
- Trim the entered string and uppercase it, so `" b "` becomes `"B"`.
- If the normalized answer is valid, return it immediately. Do not read another answer.
- Otherwise, send this exact message through `output_fn` and retry:

```text
Invalid choice. Enter A, B, C or D.
```

Example interaction:

```text
Input: "x"     → output the invalid-choice message, then ask again
Input: "  b "  → return "B" and stop
```

`input_fn` and `output_fn` are function arguments: use them so tests can supply pretend input and capture output. You do not need to replace global `input` or `print`.

If reading raises `EOFError` or `KeyboardInterrupt`, let the exception leave the function. Do not catch it and keep asking forever.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
