# Python Reloaded

**Project 01.01 · Python 3.11 or newer**

## What you are building

Build a command-line tool that edits a text file. Imagine your input file says `We waited 10 (bin) days !`. Your tool reads that file and writes `We waited 2 days!` to a second file. The original file stays as it was.

The command takes two file paths, in this order. The first file contains the text to edit. The second file is where the edited text goes. This guide uses `main.py` as the entry point. If you use a different name, document your exact command.

## Run it from start to finish

Here is a terminal session you should be able to reproduce after building the tool.

```console
$ cat sample.txts
it (cap) took 10 (bin) days ,and we found a unusual rock ! I said : ' keep it safe (up, 2) '
$ python3 main.py sample.txt result.txt
$ cat result.txt
It took 2 days, and we found an unusual rock! I said: 'keep IT SAFE'
```go-reloaded
Welcome back. Congratulations on your admission. We knew you would make it. Now it is time to get into projects.

Objectives
In this project you will use some of your old functions made in your old repository. You will use them with the objective of making a simple text completion/editing/auto-correction tool.

One more detail. This time the project will be corrected by auditors. The auditors will be other students and you will be an auditor as well.

We advise you to create your own tests for yourself and for when you will correct your auditees.

Introduction
Your project must be written in Go.
The code should respect the good practices.
It is recommended to have test files for unit testing.
The tool you are about to build will receive as arguments the name of a file containing a text that needs some modifications (the input) and the name of the file the modified text should be placed in (the output). Next is a list of possible modifications that your program should execute:

Every instance of (hex) should replace the word before with the decimal version of the word (in this case the word will always be a hexadecimal number). (Ex: "1E (hex) files were added" -> "30 files were added")

Every instance of (bin) should replace the word before with the decimal version of the word (in this case the word will always be a binary number). (Ex: "It has been 10 (bin) years" -> "It has been 2 years")

Every instance of (up) converts the word before with the Uppercase version of it. (Ex: "Ready, set, go (up) !" -> "Ready, set, GO!")

Every instance of (low) converts the word before with the Lowercase version of it. (Ex: "I should stop SHOUTING (low)" -> "I should stop shouting")

Every instance of (cap) converts the word before with the capitalized version of it. (Ex: "Welcome to the Brooklyn bridge (cap)" -> "Welcome to the Brooklyn Bridge")

For (low), (up), (cap) if a number appears next to it, like so: (low, <number>) it turns the previously specified number of words in lowercase, uppercase or capitalized accordingly. (Ex: "This is so exciting (up, 2)" -> "This is SO EXCITING")
Every instance of the punctuations ., ,, !, ?, : and ; should be close to the previous word and with space apart from the next one. (Ex: "I was sitting over there ,and then BAMM !!" -> "I was sitting over there, and then BAMM!!").

Except if there are groups of punctuation like: ... or !?. In this case the program should format the text as in the following example: "I was thinking ... You were right" -> "I was thinking... You were right".
The punctuation mark ' will always be found with another instance of it and they should be placed to the right and left of the word in the middle of them, without any spaces. (Ex: "I am exactly how they describe me: ' awesome '" -> "I am exactly how they describe me: 'awesome'")

If there are more than one word between the two ' ' marks, the program should place the marks next to the corresponding words (Ex: "As Elton John said: ' I am the most well-known homosexual in the world '" -> "As Elton John said: 'I am the most well-known homosexual in the world'")
Every instance of a should be turned into an if the next word begins with a vowel (a, e, i, o, u) or a h. (Ex: "There it was. A amazing rock!" -> "There it was. An amazing rock!").

Allowed packages
Standard Go packages are allowed.
Usage
$ cat sample.txt
it (cap) was the best of times, it was the worst of times (up) , it was the age of wisdom, it was the age of foolishness (cap, 6) , it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of darkness, it was the spring of hope, IT WAS THE (low, 3) winter of despair.
$ go run . sample.txt result.txt
$ cat result.txt
It was the best of times, it was the worst of TIMES, it was the age of wisdom, It Was The Age Of Foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of darkness, it was the spring of hope, it was the winter of despair.
$ cat sample.txt
Simply add 42 (hex) and 10 (bin) and you will see the result is 68.
$ go run . sample.txt result.txt
$ cat result.txt
Simply add 66 and 2 and you will see the result is 68.
$ cat sample.txt
There is no greater agony than bearing a untold story inside you.
$ go run . sample.txt result.txt
$ cat result.txt
There is no greater agony than bearing an untold story inside you.
$ cat sample.txt
Punctuation tests are ... kinda boring ,what do you think ?
$ go run . sample.txt result.txt
$ cat result.txt
Punctuation tests are... kinda boring, what do you think?

In this example, `(cap)` changes `it` to `It`. The binary number `10` becomes `2`. The counted uppercase command changes `it safe` to `IT SAFE`. The tool also fixes the spaces around punctuation and quotes and changes `a unusual` to `an unusual`.

## Rules your tool must follow

### 1. Change the word before a command

A command is a marker in parentheses. It tells the tool to edit text that came before it. Remove the marker from the output after applying it.

| Command | What it does | Text in the input file | Text in the output file |
| --- | --- | --- | --- |
| `(hex)` | Read the previous word as a hexadecimal number (base 16) and write it in decimal (base 10). | `1E (hex) files were added` | `30 files were added` |
| `(bin)` | Read the previous word as a binary number (base 2) and write it in decimal. | `It took 10 (bin) days` | `It took 2 days` |
| `(up)` | Uppercase every letter in the previous word. | `Ready, set, go (up) !` | `Ready, set, GO!` |
| `(low)` | Lowercase every letter in the previous word. | `Please stop SHOUTING (low)` | `Please stop shouting` |
| `(cap)` | Uppercase the first letter and lowercase the remaining letters of the previous word. | `Cross the Brooklyn bRIDGE (cap)` | `Cross the Brooklyn Bridge` |

### 2. Use a count to change several words

The case commands also accept a positive whole number after a comma, as in `(up, 2)`. Start with the word immediately before the command and count backward. Apply the change to every word in that count. Keep the words in their original order. The count form applies to `up`, `low`, and `cap`.

| Text in the input file | Text in the output file |
| --- | --- |
| `This is so exciting (up, 2)` | `This is SO EXCITING` |
| `STOP MAKING NOISE (low, 2)` | `STOP making noise` |
| `visit new york (cap, 2)` | `visit New York` |

### 3. Fix punctuation spacing

For `.`, `,`, `!`, `?`, `:`, and `;`, remove the space before the mark and leave one space before the next word when it is on the same line. Keep a group such as `...`, `!!`, or `!?` together and preserve the marks in the group.

| Text in the input file | Text in the output file |
| --- | --- |
| `Wait ,what ?` | `Wait, what?` |
| `I was thinking ... You were right` | `I was thinking... You were right` |
| `Really !? I had no idea` | `Really!? I had no idea` |

### 4. Fix spaces inside single quotes

Move the opening single quote next to the first word inside it. Move the closing single quote next to the last word inside it. Keep apostrophes inside words such as `don't` as they are. A closing quote can follow punctuation inside the quoted text.

| Text in the input file | Text in the output file |
| --- | --- |
| `She said: ' hello '` | `She said: 'hello'` |
| `He said: ' don't go yet ! '` | `He said: 'don't go yet!'` |

### 5. Change `a` to `an` before certain letters

If the next word starts with `a`, `e`, `i`, `o`, `u`, or `h`, change the separate word `a` to `an`. For capital `A`, write `An`. This exercise uses the first letter of the next word, even where everyday English would use a pronunciation rule. Leave words such as `apple` and existing uses of `an` alone.

| Text in the input file | Text in the output file |
| --- | --- |
| `There it was. A amazing rock!` | `There it was. An amazing rock!` |
| `She waited a hour.` | `She waited an hour.` |
| `He has a book.` | `He has a book.` |

## Decide and explain the order of the rules

Follow the examples above when rules appear together. In your design note, explain what order you chose for the remaining combinations. For instance, decide which word `(low)` applies to in `hello (up) (low)`, and write a test that shows your decision. Also explain whether a counted command can reach words from a previous line. Preserve text and line breaks that the rules do not affect.

## What should happen when something goes wrong

| Input or situation | Expected result |
| --- | --- |
| The input file is empty. | The command succeeds and produces an empty output file. |
| The input contains `102 (bin)` or `1G (hex)`. | Report that the number has a digit that is invalid for that base. |
| The input contains `hello (up, 2)`. | Report that the command asks for two words but only one is available. |
| The input contains `She said: ' hello`. | Report an unmatched quote. |
| The input contains `hello (cap, two)`. | Report a malformed command. |
| The input and output paths refer to the same file. | Reject the command so the input is protected. |

When a command fails, print a clear message and exit with a nonzero status. Keep the original input and any existing output intact. To check this, put some text in `result.txt`, run the program on a file containing `102 (bin)`, and open `result.txt` again. Its contents should be the same.

## How to start

1. Write down the two inputs, the output, and errors that stop the tool. Draft the steps in plain language and write at least three tests with expected results before you implement them.
2. Start with the smallest runnable version. Use a file containing `1E (hex) files were added` and check that the output says `30 files were added`.
3. Add the other rules one at a time. Keep the text editing in functions that can be tested with strings. Keep opening files and handling the terminal command in the part of your program that runs those functions.
4. Write a short note explaining where your code uses strings, files, parsing (recognizing commands in the text), and functions. Explain the order of your rules and one decision you made about how the tool should behave.

## What to use and avoid

- Use Python 3.11 or newer and the modules that come with Python for the core program. You can run tests with Python's `unittest` or use `pytest`.
- Write the implementation yourself. You can read documentation and use AI for explanations, hints, or code review. Do not copy a complete solution or use AI to generate the implementation.

## What to hand in and demonstrate

- [ ] A runnable program and the exact commands for setup, running it, and running the tests. Verify those commands from a clean checkout.
- [ ] Automated tests for `hello (up) world !` becoming `HELLO world!`, `1e (hex)` becoming `30`, the full terminal example, and the cases in the error table.
- [ ] At least two additional tests of your own. Make one a boundary case, such as `one two (up, 2)` producing `ONE TWO` when the count equals the number of words available.
- [ ] A short design note explaining the rule order, the coding concepts you used, and how you protect files when an operation fails.
- [ ] A live demo of one success and one failure without AI help. Be ready to explain how the sample travels through your program, describe a limitation, and make a small change and update its test.

## Optional extra work

Try a much larger file, record how long the tool takes, and describe one improvement your results suggest.
