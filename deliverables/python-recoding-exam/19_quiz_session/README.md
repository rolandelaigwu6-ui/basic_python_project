# Task 19 — Interactive composition and first-submission integrity

Marks: 5/100. Independent exercise.

## Required function
```python
def run_check(bank, input_fn=input, output_fn=print):
    ...
```

## Examination question

Run a six-question quiz using the supplied bank. You may assume the bank is valid. Each question has `id`, `prompt`, `options` (A–D mapped to option text) and `correct`.

For each question, in the bank's order:

1. Display its prompt and all four options using `output_fn`.
2. Read an answer using `input_fn`.
3. Trim and uppercase the answer.
4. If it is not A, B, C or D, display friendly feedback and retry that question.
5. Once the answer is valid, store it and move on, even when it is wrong. Do not offer another attempt for a valid wrong answer.

After collecting **all six answers**, ask for explanations for the first two questions. Trim each explanation and retry if it is blank. Explanations do not affect the score.

Return exactly this structure:

```python
{
    "answers": ["A", "B", "C", "D", "A", "B"],  # the six submitted choices
    "score": 4,  # example: four answers matched the bank
    "explanations": {
        "first_question_id": "First trimmed explanation",
        "second_question_id": "Second trimmed explanation",
    },
}
```

Use the actual first two question IDs as explanation keys, not the example strings above. Compute the score from the supplied correct answers.

Display the final score exactly as `Score: n/6`; for a score of 4, display `Score: 4/6`.

Example answer handling: `"x"` causes a retry; `" b "` is stored as `"B"`. If B is wrong, it still counts as the submitted answer.

Use the injected input/output functions. Let `EOFError` and `KeyboardInterrupt` propagate. Do not import implementations from another exercise folder.

## Submission
Implement solution.py. Keep supplied tests unchanged. Add a meaningful test_candidate.py and be ready to defend your choices.

## Run
```sh
python -m unittest discover -s . -p 'test_*.py' -v
```
