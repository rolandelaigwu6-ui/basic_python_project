# Production Deployment

**Mission:** 04.04  
**Language:** Python 3.11+  
**Status:** Not started

## Mission brief

Build an independently runnable implementation of production-deployment. Your deliverable must satisfy the observable behavior below, not merely demonstrate a library or reproduce a tutorial.

## Learning objectives

Study and apply: CI/CD, logging, operations. Explain where each concept appears in your implementation and why it is needed.

## Prerequisites

Be able to run Python, use Git, write functions and debug exceptions. Complete earlier missions in this phase or demonstrate equivalent knowledge. For extension projects, retain a working copy of the named base project.

## Tier 1 — Design

- Restate the contract in your own words. Identify inputs, outputs, state and failure conditions.
- Write pseudocode and at least three concrete test cases before implementing.
- Build the smallest runnable entry point and validate one normal input.

## Tier 2 — Core implementation

Deploy a previous API to a local or chosen hosting environment with automated tests, health checks and configuration.

### Acceptance example

```text
A failed test blocks deployment.
```

The example specifies behavior, not a required interface unless the contract explicitly names one. Document your exact invocation or API schema.

## Tier 3 — Robustness

Handle and test each of these cases: failed migration; missing config; unhealthy service. Return clear errors rather than silently corrupting data. Preserve valid state after a failed operation. For command-line programs, use a nonzero exit status for failures; for HTTP applications, use appropriate status codes.

## Tier 4 — Engineering challenge

Implement rollback procedure and structured logs without secrets.

Keep the core logic separate from I/O where practical. Explain your design choices and tradeoffs in a short design note.

## Tier 5 — Testing and audit

- Automate the acceptance example and every Tier 3 edge case.
- Add at least two additional cases of your own, including a boundary case.
- Run the project from a clean checkout and document setup, invocation and test commands.
- Demonstrate the core behavior and one failure live without AI assistance.

## Restrictions

- Do not copy a complete solution or use AI to generate the implementation. Use hints, documentation and reviews.
- Use appropriate documented libraries, but implement the core behavior yourself. Pin external dependencies and never commit credentials.
- Follow any more specific restrictions in the core contract. Use local fixtures or authorized systems for network and security tests.

## Peer audit questions

1. Explain the input-to-output flow for this example: A failed test blocks deployment.
2. How did you apply CI/CD, logging, operations? Show the relevant code and explain it.
3. What happens for each of these cases: failed migration; missing config; unhealthy service?
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
