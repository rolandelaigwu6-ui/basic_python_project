# Python Reloaded

**Project 01.01 · Python 3.11 or newer**

## What you are building

Build a command-line tool that edits a text file. Imagine your input file says `We waited 10 (bin) days !`. Your tool reads that file and writes `We waited 2 days!` to a second file. The original file stays as it was.

Your program accepts an input file path and an output file path. Choose how users provide them and document the exact invocation. The examples below show one possible command-line interface.

## Run it from start to finish

This terminal session uses the two transformations required by the Python assignment. The script name and argument order are examples.

```console
$ cat sample.txt
hello (up) world !
1e (hex)
$ python3 main.py sample.txt result.txt
$ cat result.txt
HELLO world!
30
```

## What to build

The Python assignment requires each feature below. The examples show what the feature can look like in practice. For details the assignment leaves open, write down your choices and test them.

### 1. Change the word before a command

A command is a marker in parentheses. It tells the tool to edit text that came before it. Remove the marker from the output after applying it.

| Command | What it does | Text in the input file | Text in the output file |
| --- | --- | --- | --- |
| `(hex)` | Read the previous word as a hexadecimal number (base 16) and write it in decimal (base 10). | `1E (hex) files were added` | `30 files were added` |
| `(bin)` | Read the previous word as a binary number (base 2) and write it in decimal. | `It took 10 (bin) days` | `It took 2 days` |
| `(up)` | Uppercase every letter in the previous word. | `Ready, set, go (up) !` | `Ready, set, GO!` |
| `(low)` | Lowercase every letter in the previous word. | `Please stop SHOUTING (low)` | `Please stop shouting` |
| `(cap)` | Capitalize the previous word. Document how you handle letters after the first one. | `Cross the Brooklyn bridge (cap)` | `Cross the Brooklyn Bridge` |

### 2. Use a count to change several words

Support counted forms of the case commands. A count of two means to change the two preceding words. The examples use a comma and a count, as in `(up, 2)`. Document the format your Python program accepts.

| Text in the input file | Text in the output file |
| --- | --- |
| `This is so exciting (up, 2)` | `This is SO EXCITING` |
| `STOP MAKING NOISE (low, 2)` | `STOP making noise` |
| `visit new york (cap, 2)` | `visit New York` |

### 3. Fix punctuation spacing

Fix spacing around punctuation. The required example shows that the space before an exclamation point is removed. Document which other marks you support and how you handle groups of punctuation. These examples show possible results.

| Text in the input file | Text in the output file |
| --- | --- |
| `Wait ,what ?` | `Wait, what?` |
| `I was thinking ... You were right` | `I was thinking... You were right` |
| `Really !? I had no idea` | `Really!? I had no idea` |

### 4. Fix spaces inside quotes

Fix extra spaces inside a pair of quotes. Choose which quote characters you support. If you support single quotes, explain how you tell an apostrophe in a word such as `don't` from a quote.

| Text in the input file | Text in the output file |
| --- | --- |
| `She said: ' hello '` | `She said: 'hello'` |
| `He said: ' don't go yet ! '` | `He said: 'don't go yet!'` |

### 5. Correct `a` and `an`

Correct the article before a word. For example, `A amazing rock` becomes `An amazing rock`, and `a book` stays `a book`. Document the rule you use and how it handles uppercase letters and cases such as words beginning with `h`.

## Decide and explain the order of the rules

Your program must pass the two acceptance examples shown in the terminal session. In your design note, explain what order you chose for the remaining combinations. For instance, decide which word `(low)` applies to in `hello (up) (low)`, and write a test that shows your decision. Also explain whether a counted command can reach words from a previous line. Preserve text and line breaks that the rules do not affect.

## What should happen when something goes wrong

| Input or situation | Expected result |
| --- | --- |
| The input file is empty. | Define the behavior and test it. For example, the command could succeed and write an empty output file. |
| The input contains `102 (bin)` or `1G (hex)`. | Report that the number has a digit that is invalid for that base. |
| The input contains `hello (up, 2)`. | Report that the command asks for two words but only one is available. |
| The input contains `She said: ' hello`. | Report an unmatched quote. |
| The input contains `hello (cap, two)`. | Report a malformed command. |

When an operation fails, report a clear error. If you build a command-line tool, exit with a nonzero status. If you expose an HTTP API, return an appropriate HTTP status. Keep the original input and any existing output intact. To check this, put some text in `result.txt`, run the program on a file containing `102 (bin)`, and open `result.txt` again. Its contents should be the same.

## How to start

1. Make sure you can run Python, use Git, write functions, and debug Python errors. Complete earlier projects in this phase or make sure you already know the skills they teach.
2. Write down the two inputs, the output, and errors that stop the tool. Draft the steps in plain language and write at least three tests with expected results before you implement them.
3. Start with the smallest runnable version. Use a file containing `1E (hex) files were added` and check that the output says `30 files were added`.
4. Add the other rules one at a time. Keep the text editing in functions that can be tested with strings. Keep opening files and handling the terminal command in the part of your program that runs those functions.
5. Write a short note explaining where your code uses strings, files, parsing (recognizing commands in the text), and functions. Explain the order of your rules and one decision you made about how the tool should behave.

## What to use and avoid

- Use Python 3.11 or newer and the modules that come with Python for the core program. You can run tests with Python's `unittest` or use `pytest`.
- Write the implementation yourself. You can read documentation and use AI for explanations, hints, or code review. Do not copy a complete solution or use AI to generate the implementation.

## What to hand in and demonstrate

- [ ] A runnable program and the exact commands for setup, running it, and running the tests. Verify those commands from a clean checkout.
- [ ] Automated tests for `hello (up) world !` becoming `HELLO world!`, `1e (hex)` becoming `30`, and every case in the error table.
- [ ] At least two additional tests of your own. Make one a boundary case, such as `one two (up, 2)` producing `ONE TWO` when the count equals the number of words available.
- [ ] A short design note explaining the rule order, the coding concepts you used, and how you protect files when an operation fails.
- [ ] A live demo of one success and one failure without AI help. Be ready to explain how the sample travels through your program, describe a limitation, and make a small change and update its test.

## Optional extra work

Try a much larger file, record how long the tool takes, and describe one improvement your results suggest.
