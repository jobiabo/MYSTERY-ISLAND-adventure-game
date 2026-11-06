# Mystery Island: AI Learning Documentary
 
AI learning log for the Mystery Island text-adventure project. Prepared 6 November 2026. Tutor and reviewer: Claude. Game-content brainstorming: ChatGPT.
 
## 1. How AI was used
 
AI was my tutor and reviewer, not the developer of the game. Two tools were used, for different jobs.
 
| Tool | Used for |
|---|---|
| Claude | Tutoring on Lessons 4 to 7 (functions, return, single responsibility, docstrings, lists vs strings, TypeError/ValueError, unittest), a code audit of my project, and the fixes in Entry 6 |
| ChatGPT | Game-design content: a review of my PLAYER_STATE names, mystery option keywords, story outcomes and scrambled-word lists |
 
How to read this log: "AI said" is a summary of the saved transcripts. "Verified" means I or the reviewer ran code to check it. Where something is not yet done, it says so.
 
Disclosure: the retry fix, the four bug fixes and the location tracking in Entry 6 were written by Claude at my request, in my coding style. I have to be able to explain every line of them in my defence.
 
Planned session schedule: Phase I 3pm to 4pm, Phase II 4pm to 5pm, Phase III 5pm to 8pm, Phase IV 8pm to 10pm, Phase V 10pm to 10:30pm, Phase VI (submission) 10:30pm.

Writing my test script to test each of my functions
 
## 2. Learning log entries
 
### Entry 1: Functions, return and single responsibility (Lesson 4)
 
**What AI said.** Single responsibility means one function has one main job. print() only shows a value; return sends a value back to the caller and ends the function immediately. A checker like can_cross_bridge should return True or False, and a different part of the program decides what story to print and whether to change energy. `return "key" in inventory` is the short form of the if/return True/return False version.
 
**My experiment.** I answered six drills in the tutoring session, all correctly on the first attempt:
 
| Drill | My answer | Result |
|---|---|---|
| Write has_key(inventory) | Wrote it myself with if/return True/return False | Correct |
| check_age(16) | B (False) | Correct |
| test() with three returns | A (10) | Correct |
| calculate(3) and calculate(8) | 13 and 16 | Correct |
| check_player() does it follow single responsibility? | B (no: it checks, prints and changes energy) | Correct |
| can_swim() has what single job? | A (check whether the player can swim) | Correct |
 
I then applied it to my game. The same retry block was copied seven times, so it became one function, ask_retry().
 
**My conclusion (draft).** A function should do one job. A checker returns a value, and another function decides what happens next. Limit: ask_retry() still prints and calls sys.exit(), so it is not a perfect single-job function. Moving the quit decision into main() is the next refactor.
 
### Entry 2: Lists vs strings, docstrings, TypeError and ValueError (Lessons 5 and 6)
 
**What AI said.** `in` on a list checks for a whole item, while `in` on a string checks for text anywhere inside it, so "key" in "monkey" is True. A docstring is the triple-quoted description straight after def, readable with `__doc__`. A TypeError means the wrong kind of data or operation; a ValueError means the right type with an unusable value, like int("banana"). Catch the specific error you expect and avoid a bare except.
 
**My experiment.** The tutor set three drills. The transcript has no answers from me yet, so this entry is not yet evidenced. Answer these before the defence:
 
1. For calculate_area(length, width): what is the function's name, its docstring, and what does it return for 5 and 4?
2. What do these four lines print? `"rope" in items`, `"key" not in items`, `"ap" in items[0]`, `"key" in "monkey"` (items = ["map", "rope", "sword"])
3. What error does int("banana") raise, and what should the game do when a player types banana instead of 1, 2, 3 or q?
**My conclusion.** Pending my answers.
 
### Entry 3: unittest (Lesson 7)
 
**What AI said.** I told the tutor I did not know unittest, TestCase, assertEqual, assertTrue or assertFalse. It explained that unittest is Python's built-in testing module, TestCase is a class that holds tests, test method names must start with test_, assertTrue and assertFalse check a condition, assertEqual compares two values, and `python -m unittest` runs them. Its drill was two tests for is_even.
 
**My experiment.** My is_even tests have not been written yet. The project folder has no tests folder.
 
**My conclusion.** Pending. The project needs at least 8 meaningful tests (T1 to T10 are recommended) run with `python -m unittest discover -s tests -v`. My stage functions mix input(), print() and decisions, so some logic must be separated before it can be tested.
 
### Entry 4: Designing the game state (ChatGPT)
 
**What AI said.** My PLAYER_STATE dictionary was a sound start. It advised player_name instead of name, has_rope and has_lantern instead of with_rope and with_lantern, deciding whether energy can go below zero and what its maximum is, and later adding current_location, health, has_map and puzzle_solved.
 
**My experiment.** I compared that advice with the final config.py. I adopted player_name, has_rope and has_lantern, and added has_map, current_location, puzzle_solved, game_progress and highest_score. The review of the whole project also found two problems the naming advice did not catch: has_rope, has_lantern and has_map are never set to True, and energy exists twice (PLAYER_STATE["health"] and a local energy_tracker in each stage).
 
**My conclusion (draft).** Good names are not enough. The state needs one source of truth that the game really updates.
 
### Entry 5: Testing the AI's puzzle words (ChatGPT)
 
**What AI said.** ChatGPT produced scrambled-word lists for the beast dodge, the beast attack, the bridge, the torch and the beacon. It twice labelled a revised list "verified".
 
**My experiment.** I compared the letters of every scramble with its answer (same letters, same counts). Verified result: 30 of 53 pairs match and 23 do not.
 
| Set | Letters match | Examples that fail |
|---|---|---|
| Dodge, first table | 4 of 10 | GDEUO to DODGE, CAVOE to EVADE |
| Dodge, "verified" set | 6 of 10 | GDEO to DODGE, ELDI to HIDE |
| Attack, first table | 2 of 10 | KICSTR to STRIKE, TAHIG to FIGHT |
| Attack, "verified" set | 8 of 10 | HSAH to SLASH, HUSLP to PUSH |
| Bridge | 2 of 3 | RUNE to TURN |
| Torch | 5 of 5 | none |
| Beacon | 3 of 5 | ZFUE to FUSE, AMEBE to BEAM |
 
What my game used instead:
 
| Stage | ChatGPT word | My game | Result |
|---|---|---|---|
| Beast dodge | GDEUO (wrong) | OGDED | Valid |
| Bridge | RUNE to TURN (wrong) | Replaced with ACPLE to PLACE | Valid |
| Torch | 5 valid words | Re-scrambled as KISCT, AGS, MAEFL, HTROC, THGIL | Valid |
| Beast attack | KICSTR to STRIKE (wrong) | KICSTRE | Not valid: extra C, could not be unscrambled to STRIKE |
 
The KICSTRE bug appears to come from ChatGPT's KICSTR, with an E added. It was found in the audit and fixed to KSTIRE. After the fix, all 16 scrambles in the game pass the same letter check.
 
**My conclusion (draft).** AI output must be checked, even when the AI says "verified". I caught several wrong words myself, but one slipped through until the audit. Next time I will check every puzzle word with a test.
 
### Entry 6: AI code review and fix loop (Claude)
 
**What AI said.** The audit measured the project against the requirements: valid choices, four locations, energy starting at 5, unique inventory items, invalid input not changing state, and functions with clear responsibilities.
 
**My experiment.** I ran scripted-input checks (a fake input() feeding answers) before and after each fix:
 
| Issue | Before | After |
|---|---|---|
| Invalid input in find_map and find_key | Energy dropped from 5 to 4 | Junk, a blank answer and 9 are re-asked; energy stays 5 until a real answer |
| Retry block | Copied 7 times | One ask_retry(); " YES " accepted, junk re-asked, "no" exits |
| Location | current_location never changed | move_to() sets jungle, old bridge and lighthouse (checked); beach is set in game_progress (not run end to end) |
| Left path | hollow_embrace() text never printed | Text prints (checked) |
| Scramble KICSTRE | Not solvable as STRIKE | KSTIRE passes the letter check |
| Replay | PLAYER_STATE kept old values | reset_player_state() is called at the start of start_game(); dirty state was reset in the test |
 
These were checked with scripted runs, not with unittest, and I have not played a full game in a real terminal.
 
**My conclusion (draft).** The Lesson 6 question "what should the game state be after a rejected input?" has a plain answer: unchanged. Wrong answers cost energy; invalid answers do not.
 
## 3. Where I am not yet at mastery
 
- There is no tests folder yet (at least 8 tests needed).
- Inventory is not real: the has_ flags are never set, and the key and torch are not tracked.
- Energy is stored in two places and each stage resets it to 5.
- The README is mostly a transcript and lacks run and test instructions.
- Entry 2 and Entry 3 drills are unanswered.
- Next lesson to cover: scope (local and global variables).
- Story text on the left path says the journey ends, but the player can retry.
- Wrong answers in find_key (options 1 and 2) cost energy but print nothing.
## 4. Defence preparation
 
These are the five defence questions from the project brief, with where my evidence is. I must write the answers myself.
 
1. Why a list for inventory? My game currently uses True/False flags, so be ready to explain both and the Lesson 5 membership idea.
2. What is the loop stopping condition? Look at the loop in main.py and the while True loop in ask_retry().
3. Show a function that returns a value rather than prints. Candidates: has_key from Entry 1, and find_map, which returns (energy_tracker, success).
4. Show a bug fixed by writing a test. Honest gap: my fixes used scripted checks. Writing unittest tests for invalid input (T2) and for puzzle-word letters would make this answer true.
5. What did AI teach you that you tested independently? Entry 5 (23 of 53 scrambles wrong) and Entry 6.
## 5. The concept I understand now that I didn't before is...
 
Draft, to be rewritten in my own words before submitting: "The concept I understand now that I didn't before is single responsibility. I used to put asking, checking, printing and changing energy in one place. Now I understand that a function should do one job and return its result, so another part of the program can decide what happens next. I saw this in my own game when seven copies of the same retry block became one function, and I know it is not finished because that function still prints and exits."
 
## 6. Submission checklist
 
- Repository URL: [https://github.com/jobiabo/MYSTERY-ISLAND-adventure-game]
- Final commit SHA: [add]
- Python version: [add; the __pycache__ in my project shows 3.12]
- How to run: `python3 main.py`
- Test command: `python -m unittest discover -s tests -v` (cannot run until the tests folder exists)
- README with setup, rules and known limits: [rewrite]
- Two AI learning-log entries: Entries 1 and 5 are the strongest; the others are drafts or pending