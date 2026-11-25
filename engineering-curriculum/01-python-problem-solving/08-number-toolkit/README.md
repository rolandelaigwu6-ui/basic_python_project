# Number Toolkit

- **Project number** 01.08
- **Use** Python 3.11+
- **Progress** Not started

## What you are building

- Convert signed whole numbers between bases 2 through 36. Write the conversion logic yourself without built-in base conversion.
- Find the GCD, the largest positive divisor shared by two numbers when one exists. Add a check for whether a number is prime.

## Before you code

1. Make sure you can run Python, use Git, write functions, and read a Python error message. Finish the earlier projects in this phase or make sure you already know the skills they teach. If this project extends an earlier one, keep a working copy of that project.
2. In your own words, write down what goes in, what comes out, what the program needs to remember, and what can fail.
3. Write pseudocode, which is a list of steps in plain language. Before writing the implementation, write at least three test cases. For each one, record the input and the result or error you expect.
4. Make the simplest version you can run and try it with one normal input.

## Example your project must pass

- Check that converting 1010 from base 2 to base 16 gives A, and that the GCD of 18 and 24 is 6.

Use any interface the project allows. If an exact route or interface is required above, use it. Write down the exact command or how to call your API, including what inputs it accepts and what it returns.

For example, Python’s int(text, base), bin(), and hex() perform the base conversion you are practicing. Write that part yourself.

## Walk through a real example

1. Convert `1010` from base 2 to base 16. The result should be `A`. Convert `A` back to base 2 and check that it returns `1010`.
2. Find the GCD of 18 and 24. The result should be 6. Check that 17 is prime and 21 is composite.
3. Try converting `102` from base 2. Expect an invalid-digit error.

## Situations you must test

- Zero.
- Negative values.
- A digit that is invalid for its base.
- Large integers.

For each situation, decide whether it is valid and write down the result you expect. If the operation fails, explain the problem and keep valid files or saved data intact. A command-line program must exit with a nonzero status on failure. A web app must return an HTTP status that matches the problem.

## Engineering work you must also finish

Implement modular exponentiation, which finds the remainder of a power after division by a modulus. Explain how the work grows as the inputs grow.

Where practical, keep the main logic in functions you can call and test separately from file access, terminal input, or web requests. Write a short design note explaining why you chose your approach, what it makes easier, and where it has drawbacks.

## What to use and avoid

- Use the Python standard library, the modules that come with Python, for the core program. You may use pytest to run tests.
- Write the implementation yourself. You may use documentation and ask AI for explanations, hints, or feedback on your work. Do not copy a complete solution or ask AI to write the implementation.
- Follow the project-specific rules above. For network or security tests, use local test files, a local test service, or a system you have permission to test. Follow any narrower testing rule in the project.

## What to hand in and show

- [ ] A runnable project that meets the requirements and passes the example.
- [ ] Automated tests for the example and every situation listed above, plus at least two tests of your own. Make one a boundary test, which checks a value at the edge of the range your program accepts.
- [ ] A short design note and a working demonstration of the engineering work.
- [ ] The exact setup, run, and test commands, verified from a clean checkout, which is a fresh copy of the project.
- [ ] A live demonstration of one success and one failure without AI help.

## Questions to practice before the review

1. Follow the example from input to output. What happens at each step?
2. Where did you use **arithmetic, algorithms**? Show the relevant code and explain why you used each one.
3. What happens in each of the situations you had to test?
4. What is your implementation’s main limitation? How could you measure it or improve it?
5. Can you make a small change to a requirement live and update its test?

## Optional extra work

Try a larger input that resembles what someone would actually use. Record how the program performs or how well it works. Explain one improvement your results suggest.
