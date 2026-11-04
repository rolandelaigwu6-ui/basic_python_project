EASY TRACK — MYSTERY ISLAND
The Lost Lighthouse | Build an interactive Python text-adventure game
FOR: absolute beginners and fellows who can use a calculator CLI but cannot yet explain variables, decisions, loops or functions confidently. This is a NEW project, not CampusFlow or a calculator. Suggested time: 6–10 focused hours across multiple learning sessions; quality and mastery matter more than speed.
START HERE — YOUR MISSION
You wake up on Mystery Island after a storm. The lighthouse is dark, the bridge is locked, and a rescue boat will arrive only if you restore the beacon. Build a text-based adventure in which the player explores locations, collects objects, solves simple puzzles and either escapes or runs out of energy.
You may use the Python standard library. No website, graphical interface, game engine, external database, or AI API. AI is your tutor and reviewer, NOT the developer who writes the entire game.
What a finished game must do
1. Display title and instructions. 2. Ask for the player's name. 3. Give choices through a menu and repeat until the player wins, loses or quits. 4. Include at least five locations: Beach, Jungle, Cave, Old Bridge, Lighthouse. 5. Track energy (starts at 5), current location and inventory. 6. Allow picking up two useful objects, such as rope and lantern, only once. 7. Include at least three meaningful decisions with consequences. 8. Require specific inventory items to cross the bridge and light the lighthouse. 9. Handle unexpected menu input without crashing. 10. End with a clear win/lose message and replay option.
Definition of done
Another fellow can run python main.py, play a complete winning path and losing path, enter invalid commands and recover, and explain what each function does. Tests run using python -m unittest discover -s tests -v. Your README states setup, game rules and known limits.
PHASE 0 — CHECK WHAT YOU ALREADY UNDERSTAND
Before starting, answer without AI: What is a variable? What is an input string? What is the difference between print() and return? When does an if condition run? Why would a while loop be helpful for a menu? If these feel difficult, start with Lesson 1; do not jump into writing the whole game.
PHASE 1 — LEARN THE REQUIRED PYTHON TOPICS FIRST
Lesson 1 | Variables, values, input and output
LEARN: variables, strings, integers, booleans, print(), input(), assignment, f-strings, basic type conversion. UNDERSTAND: input() returns a string even when someone types 3; name and current_location are strings, energy is an integer, game_running is a boolean. MINI-DRILL: ask for a player's nickname; display 'Welcome, NAME'; store score=0 and display it. CHECK: explain the type of each value and predict print(type(input(...))).
Lesson 2 | Conditions, comparisons and logical operators
LEARN: if/elif/else, ==, !=, <, <=, >, >=, and/or/not, indentation, truthiness. UNDERSTAND: a puzzle can require BOTH lantern AND rope, but a menu branch should execute only on the selected choice. MINI-DRILL: for a weather game, print 'safe' only if temperature>15 and raining is false. TEST YOURSELF: what happens if the wrong elif comes first?
Lesson 3 | Loops and control flow
LEARN: while, for, break, continue, counters, preventing infinite loops. UNDERSTAND: a menu needs to reappear after a normal choice and stop on win/lose/quit. MINI-DRILL: repeatedly ask for 'north', 'south' or 'quit'; reject anything else; terminate on quit. TEST: type blank, 'NORTH', invalid and quit; record behaviour.
Lesson 4 | Functions, parameters and return values
LEARN: def, parameters, return, scope, single responsibility, docstrings. UNDERSTAND: choose_move(), move_player(), show_inventory(), can_cross_bridge() should have separate roles. MINI-DRILL: write has_key(inventory) that returns True/False from an unrelated example. CHECK: Why should can_cross_bridge return a boolean instead of printing a whole story and changing energy?
Lesson 5 | Lists, membership and dictionaries
LEARN: lists, append, remove, in/not in, dictionaries with keys/values, .get(), list membership vs string match. UNDERSTAND: inventory can be a list; locations, game flags and player state can be a dictionary. MINI-DRILL: create items=['map']; add 'rope' if not present; print count; remove an item if present. CHECK: when would you use a dictionary instead of five unrelated variables?
Lesson 6 | Validation and friendly errors
LEARN: .strip(), .lower(), valid-choice sets/lists, TypeError/ValueError in simple terms, avoiding broad except. UNDERSTAND: ' 1 ' can be a valid menu choice after stripping; 'banana' is not. MINI-DRILL: accept only 1,2,3, or q, otherwise show a clear retry message. CHECK: what should the game state be after a rejected input?
Lesson 7 | Tiny automated tests and Git basics
LEARN: import unittest, TestCase, assertEqual, assertTrue, assertFalse; create .gitignore, README.md, git init/clone/add/commit/status and GitHub feature branches. MINI-DRILL: write two tests for a tiny function is_even(n) from your own code. CHECK: what proves that a game is correct beyond one successful playthrough?
PHASE 2 — DESIGN YOUR GAME BEFORE WRITING CODE
Draw a small map: Beach → Jungle → Cave → Old Bridge → Lighthouse. You may add backwards moves. Decide where to find the lantern and rope, which moves consume energy, which action wins, and which inputs must be rejected. Document these decisions in README.md. Game rules must be deterministic: the same state and action should have the same outcome.
Player state — recommended example
player = {'name': 'Ada', 'location': 'Beach', 'energy': 5, 'inventory': [], 'game_over': False, 'won': False}. You may choose a different representation if you explain it. Never let energy become negative; when a legal move uses the final energy point, trigger loss. Rejected/invalid input never consumes energy.
Suggested modules (not a finished solution)
main.py — starts game and handles CLI input. game.py — functions such as new_game(), available_actions(), apply_action(player, action), is_win(player). tests/test_game.py — tests for pure game functions. Keep game logic testable without requiring interactive typing.
PHASE 3 — BUILD IN SMALL, CHECKABLE MISSIONS
Checkpoint A | A single working room
Display Beach scene, show valid choices and let the player quit. Success evidence: program starts, choices are readable, and invalid input does not crash. STOP & EXPLAIN: which loop repeats the menu and why?
Checkpoint B | Movement and location
Add Jungle and Cave, and a location dictionary/map. Apply moves without inventing impossible destinations. Success evidence: Beach→Jungle→Cave; invalid direction leaves location unchanged. STOP & EXPLAIN: why is the game state stored outside the input handler?
Checkpoint C | Inventory and simple puzzle
Add rope and lantern pickups. Show inventory. Reject repeated pickups; block bridge without rope; block lighthouse lighting without lantern. Success evidence: possession gates behave correctly. STOP & EXPLAIN: what does 'in' mean for a Python list?
Checkpoint D | Energy and outcomes
Legal movement consumes 1 energy point (you can allow one free starting action if documented). Game ends with loss at energy 0 before rescue, or victory when beacon is lit with required items while energy remains. Clearly define whether visiting a location itself or a move consumes energy and test it. Add replay with a fresh new state. STOP & EXPLAIN: why should replay create a NEW inventory rather than reuse the old list?
Checkpoint E | Refactor and test
Separate input/output from game decisions so tests can call functions. Add tests. Keep one README with controls, example successful run and limitations. OPTIONAL only after core tests pass: secret collectible or second win path.
PHASE 4 — REQUIRED ACCEPTANCE TESTS
T1: new game starts at Beach with 5 energy and empty inventory. T2: an invalid command leaves player state unchanged. T3: a legal move changes location and decreases energy exactly once. T4: wrong-direction move is rejected without cost. T5: rope can be collected once. T6: bridge cannot be crossed without rope. T7: lighthouse cannot be lit without lantern. T8: correct inventory and location can win. T9: energy exhaustion causes loss. T10: replay resets energy, location and inventory. Write at least 8 meaningful unittest tests, including these critical rules; the full ten are recommended.
Bug-hunter questions
What if a fellow enters ' EXIT ' instead of 'exit'? Can energy fall to -1? Can they collect the same item twice? Can they win without going to the lighthouse? Can they replay while retaining rope? Can the player move after game_over=True?
PHASE 5 — AI AS YOUR TUTOR: COPY-READY MASTER PROMPTS
MASTER PROMPT E1 — TEACH ME THE TOPIC BEFORE CODE
Act as a patient senior Python mentor teaching an absolute beginner. I am building a text adventure called Mystery Island, but DO NOT build my game or give its full code. Teach me [TOPIC] from first principles using a tiny UNRELATED example. Explain the vocabulary, show one worked example, ask me to predict the output of two small snippets, then give me three progressive drills. Wait for my answers, evaluate my reasoning, and only reveal a corrected solution after I attempt it. When I struggle, give a hint before giving an answer. Finish by asking how this topic could apply to my game's state or choices.
MASTER PROMPT E2 — CHECKMATE MY UNDERSTANDING (ORAL EXAM)
You are my strict but supportive Python examiner. I claim I understand [VARIABLES / CONDITIONS / LOOPS / FUNCTIONS / LISTS / DICTIONARIES]. Ask me 10 questions ONE AT A TIME: 3 prediction/tracing, 3 bug-finding, 2 tiny code-writing, 2 explain-why questions. Never tell me the answer before I try. After each answer, score 0/1/2, say what was missing, and offer a follow-up if I guessed. At the end give a /20 score, the three concepts to revisit and two new practice drills. If I cannot explain why my code works, mark it not mastered.
MASTER PROMPT E3 — GUIDE, DON'T SOLVE, MY CURRENT BUG
I am building Mystery Island myself. Here is my requirement: [REQUIREMENT]. Here is the smallest relevant function and error/test result: [CODE + OUTPUT]. Do not rewrite the whole function. First ask me what I think should happen. Then give up to three hypotheses, one experiment for each, and a minimal hint. Wait for my experiment result. Help me make a failing unittest test first and explain the smallest fix after I have attempted it.
MASTER PROMPT E4 — ACT AS A PROFESSIONAL CODE AUDITOR
Act as a Python code reviewer. I will paste my Mystery Island project files and README in parts; wait until I say END OF PROJECT. Audit against these requirements: valid choices, five locations, energy starts at 5, collecting unique inventory items, a blocked bridge without rope, beacon requiring lantern, legitimate win/lose/quit/replay, invalid input not mutating state, functions with clear responsibilities, >=8 meaningful unittest tests, and executable README instructions. Do not invent results or claim to have run code unless actual execution results are provided. For each issue give severity P0/P1/P2/P3, file/function, evidence, steps to reproduce, expected vs actual, a missing test and a hint. Do not paste a replacement application. Finish with a requirement PASS/FAIL/NOT VERIFIED matrix and five questions I must answer to prove I understand the code.
MASTER PROMPT E5 — LEARNING REFLECTION AND PR REVIEW
I will show you my own Git diff or PR and test output. Review my changes like an engineer: identify one correctness risk, one readability issue, one missing test and one question about my design. Explain why each matters, but let me make the edits myself. Ask what I learned and what evidence confirms the fix. If the code is good, do not invent a defect; describe what you verified and what you could not verify.
PHASE 6 — GIT AND INDUSTRY HABITS, EVEN FOR BEGINNERS
Set up one clean repository. Suggested branch names: feat/1-game-loop, feat/2-inventory, test/3-game-rules. Meaningful commits: feat: add player movement; fix: reject invalid directions; test: cover replay reset. Use .gitignore to exclude __pycache__, .venv and generated local data. README must contain prerequisites, how to run, game rules, how to run tests and known limitations. If working in a pair, each person authors a feature PR and reviews the other's PR before merge; for solo work, request mentor/peer review rather than approving your own code.
FINAL DEMONSTRATION AND DEFENCE
Show a happy-path game, a losing path, one invalid-input path and at least eight tests. Answer: Why did you choose a list for inventory? What is the loop stopping condition? Show a function that returns a value rather than prints it. Show a bug you fixed by writing a test. What did AI teach you that you tested independently?
Success rubric — 100 marks
Gameplay and requirements 40; Python fundamentals and function design 20; testing and edge cases 15; error-handling and user experience 10; Git/README 5; AI learning evidence and individual defence 10. An impressive-looking game that the developer cannot explain is not complete.
Completion evidence to submit
GitHub repository URL, final commit SHA, Python version, main.py run instructions, unittest output, README, two AI learning-log entries (topic → what AI said → your experiment → your conclusion), and one short paragraph: 'The concept I understand now that I didn't before is...'.

