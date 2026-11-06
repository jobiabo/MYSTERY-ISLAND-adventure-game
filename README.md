# 🏝️ Mystery Island Adventure: How to Play

**The Lost Traveller** is a text-based adventure for your terminal. You wake up on a deserted beach after a storm and have to explore the island, solve puzzles and signal for rescue.

**Goal:** Survive, explore and escape Mystery Island.

---

## 1. Requirements

- Python 3 (the project was built and tested with Python 3.12)
- A terminal or command prompt
- No extra libraries needed

## 2. Starting the Game

1. Open a terminal in the `MYSTERY-ISLAND-adventure-game` folder.
2. Run:

   ```bash
   python main.py
   ```

   (Use `python3 main.py` if `python` doesn't work on your system.)
3. Press **ENTER** at the title screen.
4. Type a **nickname** when asked. It can't be left empty, and it's saved in lowercase.
5. Read the story, pressing **ENTER** to move through each screen.

---

## 3. The Basics

### ⚡ Energy
- You start every phase with **5 energy**.
- A wrong answer or a bad choice costs **1 energy**.
- At **0 energy** the game ends (**GAME OVER**).
- Each new phase begins with a "PRESS ENTER TO BOOST YOUR ENERGY" prompt that refills you to 5/5, so mistakes in one phase don't carry into the next.

### 🔁 Retrying
After a failed attempt (with energy left) the game asks:

```
Would you like to try again? (yes/no):
```

- **yes** lets you retry the same challenge.
- **no** ends the game immediately.
- Please answer exactly `yes` or `no`.

### ⌨️ Input rules
- Answers are **not case-sensitive** (`rope`, `ROPE` and `Rope` all work).
- Extra spaces around your answer are ignored.
- For choice screens you can type the **number** or the **name** of the option.
- For puzzles, answers must be entered in the **order shown**.

### 🔤 Word scrambles
Several challenges show scrambled letters, for example `EOPR`. Rearrange them into the correct word (`ROPE`) and press ENTER. In multi-word puzzles, **one wrong word fails the whole puzzle**, which costs 1 energy and you have to retry.

### 🚪 Quitting
- Press **Ctrl + C** at any time. The game asks "Do you want to quit?" so you can answer `yes` or `no`.
- After you finish the game you'll be asked if you want to play again.

---

## 4. The Journey: Phase by Phase

| Phase | Location | Challenge | Type |
|-------|----------|-----------|------|
| 1 | The Beach | Save the washing-away map | Choose 1 of 3 options |
| 2 | The Jungle | Pick a path (Left or Right) | Choose 1 of 2 paths |
| 2b | Jungle, the Beast | Dodge, then attack, the beast to earn a **rope** | 5 word scrambles |
| 3 | The Ancient Bridge | Use the rope to lower the bridge | 3 word scrambles |
| 4 | The Lighthouse | Retrieve the rusted key | Choose 1 of 3 options |
| 5 | Inside the Lighthouse | Light the torch | 5 word scrambles |
| 6 | The Jammed Door | Force the control-room door | 3 word scrambles |
| 7 | The Final Beacon | Activate the rescue signal | Press ENTER |

Complete everything to see the **rescue helicopter** ending. 🚁

---

## 5. Tips

- **Read the clues.** The option names are riddles. "Quiet" doesn't always mean "safe".
- **Think about the situation.** The scrambled words match the action in the scene (dodging, attacking, operating a wheel, lighting a torch).
- **Mind the order.** Words must be entered in the sequence they appear.
- **Don't panic after a mistake.** You can retry, but each failure costs energy, so avoid guessing blindly.
- **Typos count as wrong answers**, so double-check your spelling before pressing ENTER.
- **Choose "no" carefully.** Declining a retry quits the game.

---

## 6. Spoiler Zone: Answer Key

> ⚠️ Stuck? Open the section below. It gives away every answer, so try the game first!

<details>
<summary><b>Click to reveal the full walkthrough</b></summary>

### Phase 1: The Fading Map
| Option | Result |
|--------|--------|
| 1. Drowned Secrets | Map washed away (−1 energy) |
| 2. Treacherous Steps | You slip (−1 energy) |
| **3. Sealed Fortune** | ✅ You secure the map |

An invalid entry also costs 1 energy.

### Phase 2: The Jungle Path
| Option | Result |
|--------|--------|
| Left / 1 (The Hollow's Embrace) | Fall into a ditch (−1 energy) |
| **Right / 2 (The Predator's Trial)** | ✅ Face the beast |

### Phase 2b: The Beast
Dodge first, then attack. Enter the words in this order:

| Scramble | Answer |
|----------|--------|
| OGDED | **DODGE** |
| VOME | **MOVE** |
| TATKAC | **ATTACK** |
| KISTRE | **STRIKE** |
| ASHLS | **SLASH** |

Get both dodge words right to reach the attack round. Get all three attack words right to win and earn the **rope**.

### Phase 3: The Ancient Bridge
| Scramble | Answer |
|----------|--------|
| EOPR | **ROPE** |
| LUPL | **PULL** |
| ACPLE | **PLACE** |

### Phase 4: The Forgotten Key
| Option | Result |
|--------|--------|
| 1. The Silent Guardian | Fail (−1 energy) |
| 2. The Brittle Relic | Fail (−1 energy) |
| **3. The Keeper's Fortune** | ✅ Key secured |

### Phase 5: Ignite the Torch
| Scramble | Answer |
|----------|--------|
| KISCT | **STICK** |
| AGS | **GAS** |
| MAEFL | **FLAME** |
| HTROC | **TORCH** |
| THGIL | **LIGHT** |

### Phase 6: The Jammed Door
| Scramble | Answer |
|----------|--------|
| SUHP | **PUSH** |
| LULP | **PULL** |
| ASBLT | **BLAST** |

The intro screen shows the same words with slightly different letter orders (HSUP, LLUP, TSALB), but the answers are the same.

### Phase 7: The Final Beacon
Press **ENTER** to activate the beacon. 🎉

</details>

---

## 7. Troubleshooting

| Problem | Fix |
|---------|-----|
| `python: command not found` | Try `python3 main.py`, or install Python 3 from python.org |
| "Please provide a username" | Your nickname can't be empty |
| Answer rejected | Check spelling, and make sure you're typing in the shown order |
| Game quit unexpectedly | You answered "no" to a retry prompt, or pressed Ctrl+C |

---

**Good luck, traveller. Escape Mystery Island!** 🏝️🚁