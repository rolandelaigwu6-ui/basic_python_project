# Python Recoding Examination
## Candidate pack — assessment of a completed CampusFlow project
This is an exam, not a project-building tutorial. Solve unfamiliar problems using the concepts you should have learned while building CampusFlow. The changed domains test whether you understand the ideas rather than remember your project's functions. This is an original assessment, not an official 01Edu exam.

## Candidate rules
Work individually. Do not use AI, copy your completed project, or consult another candidate during the assessed attempt. The examiner decides beforehand whether offline Python documentation is allowed. Use only the Python standard library. Implement solution.py in each folder. Do not edit supplied tests or supplied dependencies. You may add test_candidate.py. No complete solutions are included.
Each task is independent and self-contained. A task may refer to another task's contract for a shared definition, but must never import another exercise's implementation. You can attempt tasks in any order. Functions must obey their written contracts beyond the visible examples. The examiner may add unseen tests consistent with those contracts; none are represented as already supplied.
Every task has README.md, solution.py and test_solution.py. Most stubs raise NotImplementedError intentionally: initial test failures are expected. Task 20 instead contains deliberately defective code. Passing visible tests alone does not guarantee full marks.

## Running a task
From this exam directory: python run_task.py 01_labels
Or enter that task folder and run: python -m unittest discover -s . -p 'test_*.py' -v
Run every folder in isolated processes: python run_all.py
Isolation matters because each task intentionally names its candidate module solution.py.

## Marking — 100 points
Each of 20 tasks is worth 5 points: 3 for full contract behaviour, including examiner cases; 1 for a meaningful candidate-written boundary or negative test; 1 for an individual oral explanation and a small live variation. For Task 20, the test point requires both requested original tests and the investigation record. An examiner assigns partial credit; the runners report test outcomes, not final exam marks.
Suggested administration: two sessions of 2.5 hours with a break, followed by an individual defence. Adjust time to candidate experience; this is an assessment proposal, not an official timing requirement. Record the allowed resources and time before starting.

## Oral defence
For selected tasks, explain the function's inputs, outputs, failure modes and side effects; identify the line at which mutation becomes safe; explain a boundary test; and implement a small changed rule live. Describe why bool needs special handling, why a shallow copy is insufficient for notes, why filters use AND, why JSON decoding does not establish validity, and why a rejected reload must preserve memory.

## Topics covered
Strings/Unicode; types/bools; conditions/precedence; loops; functions/return values/None; dictionaries/lists/nesting; ID generation; invariants; exceptions; state machines; validate-before-mutate; copy isolation; search/combined filters; numeric sorting; analytics/zero division; JSON syntax and schema; UTF-8 file I/O; safe persistence; migration; terminal retry loops; dependency injection/mocking; quiz scoring; unittest/temporary files; debugging and regression evidence.
Git collaboration, genuine peer review and honest AI learning records cannot be proven by a Python unit test. The separate engineering-defence.md provides an examiner-controlled assessment of those topics.

## Submission
Submit the whole folder with implementations, added tests, actual test output, Task 20 investigation, and engineering-defence.md completed with real evidence. Keep the original test files unchanged. No student name, peer review, learning experiment, pass result or repository evidence has been prefilled.
