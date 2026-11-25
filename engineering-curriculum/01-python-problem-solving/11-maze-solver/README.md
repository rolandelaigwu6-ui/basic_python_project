# Maze Solver

- **Project number** 01.11
- **Use** Python 3.11+
- **Progress** Not started

## What you are building

- Read a rectangular grid with S for start, E for exit, walls, and open cells. Document the characters you use for walls and open cells.
- Return a shortest path and its distance.

## Before you code

1. Make sure you can run Python, use Git, write functions, and read a Python error message. Finish the earlier projects in this phase or make sure you already know the skills they teach. If this project extends an earlier one, keep a working copy of that project.
2. In your own words, write down what goes in, what comes out, what the program needs to remember, and what can fail.
3. Write pseudocode, which is a list of steps in plain language. Before writing the implementation, write at least three test cases. For each one, record the input and the result or error you expect.
4. Make the simplest version you can run and try it with one normal input.

## Example your project must pass

- For S..E, check that the shortest path has distance 3.

Use any interface the project allows. If an exact route or interface is required above, use it. Write down the exact command or how to call your API, including what inputs it accepts and what it returns.

Document which moves are allowed and how you report an exit that cannot be reached. Check that every step in a returned path follows your rules.

## Walk through a real example

1. Give the solver the one-row grid `S..E`. Starting at S, move right three times to reach E. Check that the reported path and distance match.
2. Put a wall between S and E in a separate one-row grid using your wall character.
3. Check that the solver reports there is no path and returns no made-up route.

## Situations you must test

- The exit is blocked off.
- An invalid grid, such as rows with different lengths.
- More than one start.

For each situation, decide whether it is valid and write down the result you expect. If the operation fails, explain the problem and keep valid files or saved data intact. A command-line program must exit with a nonzero status on failure. A web app must return an HTTP status that matches the problem.

## Engineering work you must also finish

Compare breadth-first search, which explores nearby steps first, with depth-first search, which follows one branch before backtracking. Show the visited cells in a text grid.

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
2. Where did you use **queues, graphs, BFS**? Show the relevant code and explain why you used each one.
3. What happens in each of the situations you had to test?
4. What is your implementation’s main limitation? How could you measure it or improve it?
5. Can you make a small change to a requirement live and update its test?

## Optional extra work

Try a larger input that resembles what someone would actually use. Record how the program performs or how well it works. Explain one improvement your results suggest.
