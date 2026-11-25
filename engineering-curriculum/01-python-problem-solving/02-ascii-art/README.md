# Ascii Art

**Mission:** 01.02  
**Language:** Python 3.11+  
**Status:** Not started

## Mission brief

Build an independently runnable implementation of ascii-art. Your deliverable must satisfy the observable behavior below, not merely demonstrate a library or reproduce a tutorial.

## Learning objectives

Study and apply: loops, indexing, file parsing. Explain where each concept appears in your implementation and why it is needed.

## Prerequisites

Be able to run Python, use Git, write functions and debug exceptions. Complete earlier missions in this phase or demonstrate equivalent knowledge. For extension projects, retain a working copy of the named base project.

## Tier 1 — Design

- Restate the contract in your own words. Identify inputs, outputs, state and failure conditions.
- Write pseudocode and at least three concrete test cases before implementing.
- Build the smallest runnable entry point and validate one normal input.

## Tier 2 — Core implementation

Read a banner font with eight rows per printable ASCII character; render each input line horizontally by combining corresponding glyph rows.

### Acceptance example

```text
Input AB produces eight rows containing A and B glyphs side by side.
```

The example specifies behavior, not a required interface unless the contract explicitly names one. Document your exact invocation or API schema.

## Tier 3 — Robustness

Handle and test each of these cases: empty input; spaces; unsupported characters; missing font. Return clear errors rather than silently corrupting data. Preserve valid state after a failed operation. For command-line programs, use a nonzero exit status for failures; for HTTP applications, use appropriate status codes.

## Tier 4 — Engineering challenge

Support escaped newlines and validate font dimensions.

Keep the core logic separate from I/O where practical. Explain your design choices and tradeoffs in a short design note.

## Tier 5 — Testing and audit

- Automate the acceptance example and every Tier 3 edge case.
- Add at least two additional cases of your own, including a boundary case.
- Run the project from a clean checkout and document setup, invocation and test commands.
- Demonstrate the core behavior and one failure live without AI assistance.

## Restrictions

- Do not copy a complete solution or use AI to generate the implementation. Use hints, documentation and reviews.
- Use the Python standard library for the core implementation; pytest is optional for testing.
- Follow any more specific restrictions in the core contract. Use local fixtures or authorized systems for network and security tests.

## Peer audit questions

1. Explain the input-to-output flow for this example: Input AB produces eight rows containing A and B glyphs side by side.
2. How did you apply loops, indexing, file parsing? Show the relevant code and explain it.
3. What happens for each of these cases: empty input; spaces; unsupported characters; missing font?
4. What is the main limitation of your implementation, and how would you measure or improve it?
5. Make a small change to a requirement live, then update its test.

## Definition of done

- [ ] Core contract and acceptance example pass.
- [ ] All specified edge cases have automated tests.
- [ ] Tier 4 challenge is demonstrated.
- [ ] Setup and test instructions work from a clean checkout.
- [ ] I can explain and modify the implementation independently.

## Bonus

Benchmark or evaluate the implementation on a larger representative input, record the results and explain one improvement.
