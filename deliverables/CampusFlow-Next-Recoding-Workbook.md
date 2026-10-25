# CAMPUSFLOW NEXT
## Function-by-Function Recoding Challenge Workbook
An original exercise-based adaptation of the supplied CampusFlow Next brief. Inspired by the requested numbered-function challenge format; not an official 01Edu assessment.

## Your mission
Rebuild your understanding of the existing project one function at a time. Each exercise gives you a problem and a contract, not a solution. The difficulty comes from precise behaviour, hostile inputs, state preservation, and explaining why your code works.
Work inside the existing Python CLI repository. Preserve its working features and JSON format. Use Python standard library only: functions, dictionaries, lists, JSON, exceptions, unittest, and terminal interaction. No frameworks, databases, web APIs, authentication, paid AI services, or unnecessary class architecture.
This workbook is a practice sequence, not a replacement for the original pair-authorship, review, and submission requirements. Do not claim AI-generated work, peer reviews, experiments, or baseline results as work personally completed.

## Before Exercise 00
Record the original audited commit and inspect the repository. Identify the entry point, ticket representation, persistence format, existing functions, and tests. Run the existing application and test suite before changing anything. If the audited commit or audit report is unavailable, record that limitation; do not invent evidence.
The signatures below define practice contracts. Adapt them through small wrappers when the existing application uses different public interfaces. Do not reorganize a working repository just to match this document.

## Shared contracts — read before coding
The canonical in-memory collection in these exercises is a list of ticket dictionaries. Ticket fields: id, title, category, urgency, affected_users, priority, status, assigned_to, notes. New tickets start open, assigned_to=None, notes=[]. Categories: Network, Hardware, Software, Other. Urgencies: low, medium, high. Priorities: critical, high, medium, low. Statuses: open, in_progress, resolved.
Canonical IDs use T followed by an ASCII decimal integer formatted with at least three digits: T001, T010, T999, T1000. The number must be positive. Reject T1, T000, T0001, signs, whitespace, and non-ASCII digits. Notes use the same rule with prefix N. These stricter ID spelling rules are workbook design choices that make hidden tests deterministic; check compatibility before applying them to legacy records.
All business functions reject an incorrect Python type with TypeError and a correctly typed but invalid value with ValueError. Unknown ticket IDs raise ValueError. Missing dictionary keys raise ValueError during validation. File errors remain OSError; invalid JSON or decoded business data raises ValueError. The CLI catches expected failures and displays useful feedback.
Validate before mutation. A rejected business action must preserve the entire collection, including nested notes. Successful mutators return a detached deep copy of the updated ticket; returned data must not allow a caller to edit stored records. Read-only functions also return detached results. Validators return None unless otherwise specified.
Normalize interactive category, urgency, filter, author, title, and assignment inputs where specified. Persisted records must already be canonical: loading must not silently repair them or recompute an inconsistent priority. No timestamps or hidden counters are required. Compute each next ID from the highest existing numeric ID plus one, or 1 for an empty collection. Deletion is outside scope.
Valid transitions are open → in_progress, in_progress → resolved, resolved → open. Entering in_progress requires assignment. Same-status changes and direct open → resolved are rejected. Reopening preserves assignment and notes. Resolved tickets reject assignment changes and new notes.
Priority precedence: critical if urgency is high AND affected_users >= 10; otherwise high if urgency is high OR affected_users >= 10; otherwise medium if urgency is medium OR affected_users >= 3; otherwise low.

## How to submit each exercise
Submit the required function, focused unittest cases, and a short explanation. Before running code, write the expected output for the examples. For rejected mutations, use copy.deepcopy to snapshot the whole collection, assert the exception, and assert equality with the snapshot. For read-only operations, test both unchanged inputs and isolation of returned nested data.
Allowed dependencies include completed earlier exercises and standard-library modules. Do not call input(), print(), or open files inside business functions unless the exercise explicitly requires I/O. Do not hard-code answers for sample fixtures. Hidden checks may combine boundaries in ways the examples do not show.
For each exercise, answer: What are the valid inputs? What is returned? What can fail? What can change? Which test proves the hardest rule?

## Route map
Stage 1: diagnosis, strings, types, conditions, and IDs — Exercises 00–06.
Stage 2: dictionaries, lifecycle, and nested notes — Exercises 07–13.
Stage 3: lists, search, sorting, and counting — Exercises 14–17.
Stage 4: JSON, files, recovery, and legacy data — Exercises 18–22.
Stage 5: terminal I/O, quiz, and integration — Exercises 23–28.
Final gates: regression evidence, bug hunting, pair review, learning records, and live defence.
Write a diagnostic helper that returns the Python version, whether the configured data file exists, and the detected ticket count through the existing loader. Do not modify the data file. Keep command execution and reporting in a separate script. Capture the old application run command, unittest command, actual results, three manual inputs, and audit observations in docs/baseline-check.md. A peer-reported defect becomes confirmed only after reproduction.

## Exercise 00 — Baseline witness

### Required function
baseline_probe() -> dict

### Challenge
Write a diagnostic helper that returns the Python version, whether the configured data file exists, and the detected ticket count through the existing loader. Do not modify the data file. Keep command execution and reporting in a separate script. Capture the old application run command, unittest command, actual results, three manual inputs, and audit observations in docs/baseline-check.md. A peer-reported defect becomes confirmed only after reproduction.

### Observable examples
Three manual probes: create a valid ticket; attempt an invalid affected_users value; attempt a lifecycle action. Record actual behaviour even when it is wrong.

### Required checks
Run python -m unittest discover -s tests -v at the baseline revision. Preserve the actual output and commit SHA.

### Defence question
What evidence distinguishes an observed failure from an unverified audit claim?

## Exercise 01 — Clean label

### Required function
clean_label(value, field_name) -> str

### Challenge
Accept strings only. Trim leading and trailing whitespace; reject an empty result. Keep internal whitespace and letter case. Use field_name in a useful failure message. Do not convert arbitrary objects to strings.

### Observable examples
clean_label("  Mentor A  ", "author") returns "Mentor A"; whitespace-only input raises ValueError; None raises TypeError.

### Required checks
Include empty text, tabs/newlines, internal spaces, integers, and a valid Unicode label.

### Defence question
Why does str(None) violate this contract?

## Exercise 02 — Canonical choice

### Required function
normalize_choice(value, allowed) -> str

### Challenge
allowed is a nonempty tuple of unique canonical strings with no casefold collisions. Validate that configuration. Match value after strip and casefold, then return the original canonical member. Reject nonstrings and unknown choices.

### Observable examples
normalize_choice(" network ", ("Network", "Hardware", "Software", "Other")) returns "Network".

### Required checks
Test invalid configuration, unknown option, empty input, and mixed case.

### Defence question
Why should storage use one spelling even if the CLI accepts many?

## Exercise 03 — The boolean trap

### Required function
validate_affected_users(value) -> None

### Challenge
Accept only a built-in int greater than zero. Explicitly reject booleans, floats, numeric strings, None, and integer subclasses. Never coerce the input.

### Observable examples
1 passes; 0 and -1 raise ValueError; True, 1.0, and "1" raise TypeError.

### Required checks
Use subTest to cover every rejected type and boundaries 1, 3, 10.

### Defence question
Why is isinstance(True, int) insufficient here?

## Exercise 04 — Priority tribunal

### Required function
calculate_priority(urgency, affected_users) -> str

### Challenge
Validate and normalize urgency with Exercise 02, then validate affected_users. Apply the exact shared precedence. Keep this function pure.

### Observable examples
("high",10) → critical; ("high",1) → high; ("low",10) → high; ("low",3) → medium; ("low",2) → low.

### Required checks
Cover urgency × affected_users values 1, 2, 3, 9, 10, 11, and invalid inputs.

### Defence question
Which overlapping conditions make if/elif order observable?

## Exercise 05 — Identifier interpreter

### Required function
parse_identifier(value, prefix) -> int

### Challenge
Validate an ID using the shared spelling rule. prefix must be T or N. Return its numeric portion. Do not accept Unicode decimal lookalikes or alternate zero padding.

### Observable examples
T002 → 2; T1000 → 1000; T2, T000, T0002, and " T002" fail for prefix T.

### Required checks
Include prefix mismatch, embedded spaces, negative signs, nonstrings, and full-width digits.

### Defence question
How will your code distinguish a valid number from a valid ID?

## Exercise 06 — Next available number

### Required function
next_ticket_id(tickets) -> str

### Challenge
Validate each existing ticket ID and reject duplicate IDs. Scan the whole list; return highest numeric ID plus one. Do not rely on list length or ordering. Empty input returns T001. This function checks IDs only, not full ticket bodies.

### Observable examples
IDs T010, T002, T100 produce T101; T999 produces T1000.

### Required checks
Use gaps, unsorted IDs, duplicates, empty input, and a malformed ID late in the list.

### Defence question
Why can len(tickets)+1 collide?

## Exercise 07 — A complete invariant

### Required function
validate_ticket(ticket) -> None

### Challenge
Require all ten schema keys; allow additional keys for compatibility. Validate canonical nonblank trimmed title, category, urgency, affected_users, calculated priority, legal status, assignment, and notes. assigned_to is None or a trimmed nonblank string. in_progress and resolved require assignment. Validate notes as a list of dictionaries containing note_id, author, message; require unique valid note IDs per ticket, trimmed nonblank authors, and trimmed messages of 5–300 characters. Extra note keys are allowed. Do not modify the record.

### Observable examples
A stored urgency "HIGH", mismatched priority, duplicate note ID, or resolved unassigned record must fail.

### Required checks
Change one invariant at a time in a valid fixture; include nested note failures.

### Defence question
Why can valid JSON still describe an invalid ticket?

## Exercise 08 — Create without damage

### Required function
create_ticket(tickets, title, category, urgency, affected_users) -> dict

### Challenge
Validate the existing collection, normalize new inputs, allocate an ID, construct all required fields, and append only after every check succeeds. Return a detached copy of the created ticket.

### Observable examples
First valid ticket is T001, open, unassigned, with an empty notes list. A rejected second create does not consume T002.

### Required checks
Snapshot the entire collection for invalid category, blank title, float, bool, and invalid existing data.

### Defence question
At what exact statement does mutation become safe?

## Exercise 09 — Assignment guard

### Required function
assign_ticket(tickets, ticket_id, staff_label) -> dict

### Challenge
Validate the collection and ID, find the ticket, clean the staff label, and reject resolved tickets. Allow assignment or reassignment on open/in_progress tickets. Preserve every other field.

### Observable examples
Assign "  Operator B  " to open T001 → assigned_to="Operator B". Assignment on resolved T001 fails.

### Required checks
Unknown ID, blank label, nonstring label, reassignment, and mutation of the returned copy.

### Defence question
Can validation order accidentally mutate state before an error?

## Exercise 10 — Transition gate

### Required function
can_transition(ticket, new_status) -> bool

### Challenge
Validate the ticket and require a canonical legal new_status. Return True only for an allowed edge whose assignment precondition holds. Return False for same status, skipped steps, or unassigned open → in_progress. Malformed inputs raise errors rather than returning False.

### Observable examples
Unassigned open → in_progress is False; assigned open → in_progress is True; assigned open → resolved is False.

### Required checks
Test every pair in the three-by-three status matrix and the assignment condition.

### Defence question
Why distinguish an invalid record from a valid record with a forbidden transition?

## Exercise 11 — State machine mutation

### Required function
change_status(tickets, ticket_id, new_status) -> dict

### Challenge
Validate the collection and requested canonical status, then use the transition gate. Reject forbidden moves with ValueError. On success update only status and return a detached copy.

### Observable examples
open → in_progress → resolved → open succeeds when assigned. Notes survive the entire route.

### Required checks
Prove unassigned transition rejection preserves the whole collection; verify reopen keeps assignment and notes.

### Defence question
Which tests prevent a future shortcut from allowing open → resolved?

## Exercise 12 — Note sequence

### Required function
next_note_id(ticket) -> str

### Challenge
Validate the ticket and derive the next note ID from the highest numeric note ID, not the list position. Do not append anything.

### Observable examples
No notes → N001; N002 and N010 → N011; N999 → N1000.

### Required checks
Include unsorted notes, gaps, duplicate note IDs, and invalid note shapes.

### Defence question
Why should a rejected note have no effect on this result?

## Exercise 13 — Controlled follow-up

### Required function
add_note(tickets, ticket_id, author, message) -> dict

### Challenge
Validate collection and ticket identity; reject resolved tickets. Trim author and message, require nonblank author and 5–300 characters in the trimmed message. Only then compute and append the note. Return a detached copy of the updated ticket.

### Observable examples
Open T001 receives N001. A four-character message fails; the next accepted message is N002. Resolve rejects a note; reopen allows the next ID.

### Required checks
Test lengths 4, 5, 300, 301 after trimming; nonstrings; resolved ticket; alias isolation.

### Defence question
How do you prove a failed action did not consume an ID?

## Exercise 14 — Read notes safely

### Required function
get_ticket_notes(tickets, ticket_id) -> list

### Challenge
Validate the collection and return detached notes in ascending numeric note-ID order. An unknown ticket is an error; an existing ticket with no notes returns an empty list. Never sort the stored list in place.

### Observable examples
Stored order N010, N002 returns N002, N010. Editing a returned message must not edit storage.

### Required checks
Snapshot stored order, alter returned nested data, and check unknown/empty cases.

### Defence question
Why is list(ticket["notes"]) insufficient isolation?

## Exercise 15 — Search intersection

### Required function
search_tickets(tickets, title="", category="", status="", priority="") -> list

### Challenge
Validate collection and all string filter arguments. Trim title and use casefold substring matching; empty title matches all. Normalize nonempty category/status/priority filters to their canonical choices. Whitespace-only filters are empty. Every supplied filter must match. Preserve input order and return detached tickets. Invalid options raise errors even for an empty dataset.

### Observable examples
Title "WI-FI", category "network", status "open" matches only open Network tickets containing "wi-fi". "wifi" need not match "wi-fi".

### Required checks
Case differences, Unicode casefold, no matches, all filters combined, invalid filter on empty data, and nested-result isolation.

### Defence question
Why is OR wrong when users narrow results?

## Exercise 16 — Two queues, two promises

### Required function
open_work_queue(tickets) -> list; sort_search_results(results) -> list

### Challenge
Implement two separate pure functions using priority rank then numeric ticket ID. The original queue includes only open tickets. The optional search sorter retains all supplied results, regardless of status. Both return detached dictionaries without rearranging their inputs.

### Observable examples
For equal priority, T002 precedes T010. An in_progress critical ticket is excluded from the open queue but retained by the search sorter.

### Required checks
Mixed statuses, every priority, numeric ties, unsorted input, and no mutation.

### Defence question
How could reusing the wrong filter silently break the original feature?

## Exercise 17 — Reports that reconcile

### Required function
build_report(tickets) -> dict

### Challenge
Validate records. Return total, by_status, by_priority, by_category, unresolved, resolved, resolution_percentage. Include every canonical bucket with zero defaults. unresolved=open+in_progress. Percentage is resolved/total*100, or 0.0 when empty; leave rounding to display. Count current status only.

### Observable examples
One open, one in_progress, one resolved → total 3, unresolved 2, resolved 1, percentage approximately 33.3333. Reopen the resolved ticket → resolved 0.

### Required checks
Empty data, all resolved, all categories, reopen, and sum of each count mapping equals total. Use assertAlmostEqual for percentages.

### Defence question
Why must report generation avoid relying on past transitions?

## Exercise 18 — Collection checkpoint

### Required function
validate_collection(tickets) -> None

### Challenge
Require a list, validate every ticket, and reject duplicate ticket IDs. Note IDs must be unique within one ticket, but N001 may appear on different tickets. Additional keys remain supported. Leave inputs unchanged even when a late record fails.

### Observable examples
T001/N001 and T002/N001 are valid; two T001 records are invalid.

### Required checks
Wrong top-level type, non-dictionary entries, a bad last record, duplicate ticket IDs, and note-ID scope.

### Defence question
Why is validating only the first record unsafe?

## Exercise 19 — Decode without trust

### Required function
decode_tickets(text) -> list

### Challenge
For the practice format, decode a JSON list and validate the full collection before returning it. For the actual repository, retain its existing envelope through a documented adapter. Do not modify current memory or touch files. Preserve valid extra fields. Reject duplicate JSON object member names instead of silently accepting the final value.

### Observable examples
"[]" returns []; malformed JSON, duplicate ticket IDs, a root object in list mode, and repeated "status" keys fail.

### Required checks
JSON null, scalar roots, booleans as affected_users, missing keys, duplicate members, and inconsistent priority.

### Defence question
What is the difference between JSON syntax validation and business validation?

## Exercise 20 — Load as a transaction

### Required function
load_tickets(path) -> list; reload_tickets(current, path) -> None

### Challenge
load_tickets reads UTF-8 and decodes into a temporary collection. reload_tickets replaces current contents only after the entire load succeeds, preserving the identity of the current list. Do not treat missing or invalid files as empty datasets. File errors remain visible to the caller.

### Observable examples
A file with one good record followed by one duplicate leaves current unchanged. A successful reload makes next_ticket_id and next_note_id continue correctly.

### Required checks
Use tempfile.TemporaryDirectory for missing files, broken JSON, invalid late records, valid reload, and list identity preservation.

### Defence question
Which operation commits the new state?

## Exercise 21 — Save without truncation

### Required function
save_tickets(tickets, path) -> None

### Challenge
Validate before writing. Encode complete UTF-8 JSON including notes and extra fields. Write a temporary file in the destination directory, close it, then use os.replace. Clean up the temporary file on failure. Preserve an existing destination if validation, serialization, or replacement fails. Atomic replacement reduces partial-write risk; do not claim a power-loss durability guarantee.

### Observable examples
A valid round trip preserves ticket and note IDs. An unserializable extra field must fail before replacing the old file.

### Required checks
Valid round trip, invalid data with existing file, serialization failure, and mocked replacement failure with cleanup.

### Defence question
Why is opening the destination in write mode too early dangerous?

## Exercise 22 — Legacy bridge

### Required function
upgrade_legacy_tickets(records) -> list

### Challenge
Use this adapter only if the original schema lacks notes. Work on a detached copy, add notes=[] only where the key is absent, validate the resulting collection, and return it. Do not overwrite an existing notes value or repair unrelated errors. Keep original source files untouched; write migrated data to a distinct path after explicit CLI selection. Document supported formats.

### Observable examples
An otherwise valid old ticket gains notes=[]. notes=None is rejected, not replaced.

### Required checks
Original nested data unchanged, absent notes, invalid existing notes, duplicates, and already upgraded records.

### Defence question
How do you prove migration protects the original evidence?

## Exercise 23 — Input boundary

### Required function
read_choice(prompt, allowed, input_fn=input, output_fn=print) -> str

### Challenge
Require a nonempty tuple of distinct uppercase single-letter options. Read, strip, uppercase, and retry until a permitted choice is entered. Print a friendly retry message for invalid answers. Propagate EOFError and KeyboardInterrupt so the application boundary can exit cleanly.

### Observable examples
Inputs "X", "", " b " with allowed A/B/C/D return B after two retries.

### Required checks
Inject fake input/output functions; assert number of reads, returned value, and retry feedback.

### Defence question
Why is terminal input normalization different from accepting floats in a business function?

## Exercise 24 — Scores without a menu

### Required function
score_answers(question_bank, answers) -> int

### Challenge
Keep the six required questions in a separate bank: stable IDs Q1–Q6, prompt, four labelled options A–D, and correct answer. Require one canonical answer per question. Validate bank structure, unique question IDs, complete options, valid keys, answer count, and answer values. Return one point per correct first answer. No input or output here.

### Observable examples
Correct key: Q1 B, Q2 C, Q3 B, Q4 C, Q5 C, Q6 B. All correct → 6; all incorrect → 0.

### Required checks
Partial scores, mismatched lengths, invalid option, duplicate question ID, malformed options, and no input mutation.

### Defence question
How does separating data from scoring prevent menu-specific scoring mistakes?

## Exercise 25 — Understanding interview

### Required function
run_understanding_check(question_bank, input_fn=input, output_fn=print) -> dict

### Challenge
Display all six questions, collect validated first answers through read_choice, and score using score_answers. Then ask for nonblank explanations for Q1 and Q5; retry blank explanations. Return answers, score, and explanations and display them for mentor discussion. Do not auto-grade explanations or allow feedback to change submitted answers.

### Observable examples
An invalid X followed by B counts as submitted B. A valid wrong A followed by feedback remains a wrong answer.

### Required checks
Script the complete session, invalid retries, exact score, two explanations, and unchanged question bank.

### Defence question
Why is keyword matching insufficient evidence of understanding?

## Exercise 26 — Notes at the terminal

### Required function
add_note_cli(tickets, input_fn=input, output_fn=print) -> None; view_notes_cli(tickets, input_fn=input, output_fn=print) -> None

### Challenge
Use the business APIs to add and retrieve notes. Prompt for the required fields, show useful failures, and return to the menu without crashing. Display notes in numeric ID order with author and message. Do not duplicate business validation in the menu.

### Observable examples
A resolved-ticket attempt prints why it was rejected and preserves notes. Empty notes prints a clear message.

### Required checks
Mock/inject I/O for valid note, invalid message, unknown ticket, resolved rejection, and ordered display.

### Defence question
Where should the resolved-ticket rule live so every caller obeys it?

## Exercise 27 — Search and report screens

### Required function
search_cli(tickets, input_fn=input, output_fn=print) -> None; reports_cli(tickets, output_fn=print) -> None

### Challenge
Prompt for optional title/category/status/priority filters. Re-prompt invalid filter choices; display ID, title, category, priority, status, assigned_to. Offer a separate priority-sorted search display. Reports show every required count and percentage, formatted to two decimal places. Keep the original open queue menu separate.

### Observable examples
Blank filters show all tickets. Empty reports display 0.00%. Invalid status "closed" triggers retry.

### Required checks
Script invalid filter retry, AND filtering, no matches, optional sorting, report totals, and unchanged state.

### Defence question
How do you test printed behaviour without repeatedly typing?

## Exercise 28 — Integration defence

### Required function
main(input_fn=input, output_fn=print) -> None

### Challenge
Integrate existing creation, assignment, status workflow, open queue, reports, JSON save/load, and all new menus. Add Engineering Understanding Check. Separate routing from business logic; catch expected errors at an appropriate boundary. Handle EOF/interrupt gracefully without silently saving over source data. Retain existing application behaviour unless a documented reliability requirement changes it.

### Observable examples
Demonstrate create → assign → in_progress → note → resolve → reject note → reopen → note → save → restart → reload → next IDs.

### Required checks
Run the full suite from a fresh checkout; exercise invalid menu choices, failed reload with existing memory, and original queue regression.

### Defence question
If the mentor changes a rule, which single function and focused tests should change?

## Required question bank
Keep these scenarios and answer options in the separate bank; the scoring function must not hard-code scenario-specific branches.
Q1. T001 is open and unassigned. A user requests in_progress. A: Accept. B: Reject and preserve all data. C: Resolve automatically. D: Remove ticket.
Q2. The app has zero tickets. What resolution percentage should display? A: Crash. B: 100%. C: 0%. D: Divide by one without explanation.
Q3. Filter title='wifi', category='Network', status='open'. Which records match? A: Any one filter. B: All supplied filters. C: All Network records. D: All open records.
Q4. A resolved ticket receives Add note. A: Append anyway. B: Delete old notes. C: Reject until reopened. D: Change status silently.
Q5. JSON includes two tickets with the same ID. A: Keep both. B: Replace memory with duplicates. C: Reject without changing memory. D: Rename IDs silently.
Q6. A PR changes validation without negative tests. A: Approve because it runs. B: Request focused tests and reasoning. C: Merge immediately. D: Ask AI to approve.

## Final gate A — Minimum evidence suite
Run: python -m unittest discover -s tests -v
Include at least fourteen meaningful tests, with at least five genuinely authored by each engineer. A high test count alone does not prove coverage. The final suite must explicitly cover all fourteen original acceptance cases: priority precedence; unassigned transition rejection with unchanged data; resolved assignment rejection; invalid affected_users; valid note ID; invalid note without ID consumption; resolved-note rejection and reopened-note acceptance; case-insensitive substring search; combined AND filters; empty report; report correctness after reopen; persistence and next IDs; corrupt JSON and duplicate ticket IDs without state loss; invalid quiz input and correct scoring.
Also preserve original regression tests. Do not rename a new test as historical evidence or claim it failed before a fix unless you actually observed that failure.

## Final gate B — Two unseen bug hunts
Engineer A devises one previously unlisted edge case for Engineer B's module. Engineer B does the same for Engineer A. Keep the challenge undisclosed until the recipient predicts behaviour. Record initial state, input, expected result, actual result, test name, and any code change. If the test passes immediately, record that honestly. Do not reuse a listed boundary and call it a new discovery.

## Final gate C — Real pair engineering
Engineer A owns validation, safe mutations, note business logic, persistence, and ID continuity. Engineer B owns search, reports, note CLI, retry behaviour, and understanding check. Agree on interfaces first. Helpers may be shared; authorship must remain truthful.
Open real issues in the existing GitHub repository. Use feature branches with actual issue IDs. Each engineer makes at least two focused commits and one substantial PR with source and tests. Each reviews the other's diff, runs relevant tests, leaves at least two specific observations, and records approval before merge. Address blocking feedback and rerun tests. Never manufacture partner identity, review comments, approval, or merge evidence. If branch protection is available, require PR approval; otherwise retain review chronology for mentor verification.
After integration, run tests on final main and from a fresh checkout. Record the exact SHA and command output. Do not make direct feature commits to main.

## Final gate D — AI learning record
Each engineer records two real learning cycles in docs/ai-learning-log.md. For each cycle record: prior belief/concept gap; exact question asked; guidance received; tiny unrelated experiment; independent documentation/test evidence; result; final engineering decision; guarding test. At least one team cycle must show a suggestion changed or rejected after evidence review. Do not invent a mistaken suggestion to satisfy the requirement.
Suggested unrelated experiments: book-label normalization; shopping-quantity boolean validation; a nested music-playlist copy; a corrupted reading-list JSON file; casefold versus lower on unrelated words. Run the experiment and record actual results before writing the conclusion.

## Individual defence card
Without AI assistance, each engineer must explain an invariant their code guarantees; show one genuinely observed failed test and correction; prove unchanged state after rejection; demonstrate duplicate-ID load failure; explain AND filtering; describe a verified AI claim; show substantive partner review; and locate the function and tests affected by a mentor's changed rule. Each takes the six-question CLI independently and explains two answers using actual code.

## Submission checklist
Engineer A full name; Engineer B full name; existing repository URL; audited baseline SHA; final main SHA; both feature PR URLs; actual unittest output; README with fresh-clone commands and JSON format; docs/baseline-check.md; docs/ai-learning-log.md; documented design choices and compatibility limits; bug-hunt records; individual reflections; final CLI demonstration.
Each reflection describes one verified mistake, one learning gain, and one improvement received through review. If failures remain, record them and seek mentor support rather than claiming completion.

## Assessment alignment — 100 points
Original features and baseline evidence: 10. Validation/lifecycle: 15. Follow-up notes: 10. Search/reports: 15. Safe JSON and ID continuity: 10. Meaningful tests and bug hunts: 15. Real branches, authorship, review, and approved merges: 15. Verified learning, understanding check, documentation, and defence: 10.
Completion requires both working software and evidence that both engineers understand it.

## Suggested use in the eight-hour sprint
Session 1: baseline and repository inspection; focused concept experiments; contract agreement and issues; implementation of each engineer's owned functions with initial tests. Session 2: remaining CLI integration and negative tests; real reciprocal PR reviews; fixes and merged-suite verification; documentation and individual defence.
There are more exercises than a novice pair may finish independently in eight hours. Use existing correct functions as candidates for recoding and defence rather than rewriting them unnecessarily. Mentors may select practice exercises, but the final application must still meet every original acceptance requirement. The workbook can also be used as a longer individual study sequence.

## Google Docs import
Upload the accompanying .docx to Google Drive and open it with Google Docs. Use File → Save as Google Docs if conversion is needed. Keep the Markdown copy as a plain-text source for future revisions.
