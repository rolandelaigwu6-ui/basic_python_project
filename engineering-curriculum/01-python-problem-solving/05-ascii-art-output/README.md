# Ascii Art Output

- **Project number** 01.05
- **Use** Python 3.11+
- **Progress** Not started

## What you are building

- Let the user write the rendered art to a named file or print it in the terminal through standard output.
- Decide what happens when the output file already exists, and document that choice.

## Before you code

1. Make sure you can run Python, use Git, write functions, and read a Python error message. Finish the earlier projects in this phase or make sure you already know the skills they teach. If this project extends an earlier one, keep a working copy of that project.
2. In your own words, write down what goes in, what comes out, what the program needs to remember, and what can fail.
3. Write pseudocode, which is a list of steps in plain language. Before writing the implementation, write at least three test cases. For each one, record the input and the result or error you expect.
4. Make the simplest version you can run and try it with one normal input.

## Example your project must pass

- With --output=hello.txt Hello, check that hello.txt contains eight glyph rows.

Use any interface the project allows. If an exact route or interface is required above, use it. Write down the exact command or how to call your API, including what inputs it accepts and what it returns.

## Walk through a real example

1. Render `Hello` with `--output=hello.txt` and open the file. Count eight rows of artwork.
2. Render the same text without an output path. Compare the terminal art with the file contents.
3. Put known text in an existing destination and exercise your documented overwrite rule. If an attempt fails, check that its old text is intact.

## Situations you must test

- An existing output file.
- A directory where the program cannot write.
- An empty text input.

For each situation, decide whether it is valid and write down the result you expect. If the operation fails, explain the problem and keep valid files or saved data intact. A command-line program must exit with a nonzero status on failure. A web app must return an HTTP status that matches the problem.

## Engineering work you must also finish

Use atomic replacement. Write the complete result to a temporary file, then replace the destination in one operation when your overwrite policy allows it. Handle failed writes without leaving a partial result at the destination.

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
2. Where did you use **file I/O, CLI flags**? Show the relevant code and explain why you used each one.
3. What happens in each of the situations you had to test?
4. What is your implementation’s main limitation? How could you measure it or improve it?
5. Can you make a small change to a requirement live and update its test?

## Optional extra work

Try a larger input that resembles what someone would actually use. Record how the program performs or how well it works. Explain one improvement your results suggest.
