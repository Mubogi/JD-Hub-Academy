# Module 1 — Thinking Like a Computer

Before a child touches a computer, they need one idea: a computer does exactly
what it is told, in the order it is told, and nothing else. That is not a
limitation to be frustrated by. It is the whole game. Once you see it, you can
make it do anything.

Scratch is a programming language made of blocks that snap together. You cannot
make a syntax error, so every mistake is a logic mistake — which is exactly the
mistake worth learning to find.

::: scripture
"Let all things be done decently and in order."
— 1 Corinthians 14:40
:::

Order is the first lesson of programming and the last lesson of life. A program
that is out of order does not work, no matter how good each part is.

## Lesson 1.1 — What a program is

A program is a list of instructions, executed in sequence, by something that has
no common sense. That last part matters. A human can guess what you meant; a
computer cannot.

**The sandwich test.** Write instructions for making a sandwich as if for someone
who has never seen one. "Put the butter on the bread" — which bread? How much
butter? With what? The moment you find the ambiguity, you have understood
programming.

## Lesson 1.2 — The Scratch workspace

Three areas. Learn them in five minutes.

**The stage** — top left. Where your program runs.
**The sprite list** — bottom left. The characters and objects.
**The block palette and script area** — right. The blocks, and where you build.

Every block snaps only to blocks it can connect to. That is Scratch's way of
teaching you structure without punishing you for typos.

## Lesson 1.3 — Your first program

Four blocks produce a working program:

```
when [green flag] clicked
  move 10 steps
  say "Hello!" for 2 seconds
  play sound [pop]
```

Press the green flag. Something happened, in order, because you said so.

That is the entire concept of programming, and everything after this is detail.

::: exercise
**Exercise 1.3 — Make it move**

1. Add a sprite (any character).
2. Make it move 100 steps when the green flag is clicked.
3. Make it say its own name afterwards.
4. Change the number to 10. What happens? Change it to 1000. What happens?
5. Write one sentence: what does the number control?

**Time:** 20 minutes. **Deliverable:** a working script and one sentence.
:::

# Module 2 — Sequence and Loops

## Lesson 2.1 — Sequence

Sequence is the order of instructions. Change the order, change the result.

The classic demonstration: draw a square by moving and turning. Move, turn, move,
turn, move, turn, move, turn. Four of each. It works, and it is tedious — which is
exactly the point, because tedium is what loops exist to remove.

## Lesson 2.2 — Loops

A loop repeats instructions. The square becomes:

```
repeat 4
  move 100 steps
  turn 90 degrees
```

Four lines become two, and — crucially — the intent becomes visible. Anyone
reading it can see "this is a square" rather than counting four pairs of blocks.

That is the real value of a loop. It is not just shorter. It expresses what you
meant.

## Lesson 2.3 — Nested loops

A loop inside a loop draws patterns. This is where children's faces change,
because the output becomes something they did not directly instruct.

```
repeat 12
  repeat 4
    move 50 steps
    turn 90 degrees
  turn 30 degrees
```

Twelve squares, rotated. A flower. Nobody wrote "draw a flower". The logic
produced it.

::: exercise
**Exercise 2.3 — Shape explorer**

1. Draw a triangle (three sides, 120-degree turns).
2. Draw a hexagon (six sides, 60-degree turns).
3. Draw a circle using 360 repeats of 1 step and 1 degree.
4. Make a pattern by nesting a loop.
5. Write down the rule: what does the turn angle have to be for a shape to close?

**Time:** 30 minutes. **Deliverable:** four shapes and the rule.
:::

# Module 3 — Variables and Conditionals

## Lesson 3.1 — Variables

A variable is a labelled box that holds a value. A score. A lives count. A
player's name.

In Scratch: make a variable, then use `set` to put something in it and `change` to
add to it. Show it on the stage so the player can see it.

## Lesson 3.2 — Conditionals

A conditional makes a decision: **if** something is true, **then** do this.

```
if <touching [edge]?> then
  say "Ouch!" for 1 second
  move -20 steps
```

The `else` branch handles the other case. The combination of variables and
conditionals is where programs stop being demonstrations and start being games.

## Lesson 3.3 — The score system

The most motivating thing a child can build: something that keeps score.

```
when [green flag] clicked
  set [score] to 0
forever
  if <touching [coin]?> then
    change [score] by 1
    go to [random position]
```

Now the program has state — a memory of what has happened — and the child
immediately wants to make it better. That wanting is the whole curriculum.

::: exercise
**Exercise 3.3 — Catch the coin**

1. Make a coin sprite that moves to a random position when touched.
2. Add a score variable, visible on the stage.
3. Add a time limit using a second variable that counts down.
4. Add a "game over" message when time reaches zero.
5. Play it. Then fix the thing that annoys you most.

**Time:** 40 minutes. **Deliverable:** a playable game with a score.
:::

# Module 4 — Events, Broadcasts and Coordination

## Lesson 4.1 — Events

An event is a trigger: the green flag, a key press, a click, a message. Events are
how separate scripts cooperate.

Every sprite can have its own scripts, all running at once. The green flag starts
them all. That parallel structure is genuinely powerful and is the concept most
transferable to real programming.

## Lesson 4.2 — Broadcast

Broadcast is how one sprite tells the others something happened.

```
broadcast [start game]
```

And in another sprite:

```
when I receive [start game]
  show
  go to x:0 y:0
```

This is the mechanism for scenes, levels, and any multi-part story. It is also,
quietly, the same idea as an event in a web application, which is why learning it
in Scratch transfers later.

## Lesson 4.3 — A conversation

Two sprites, alternating, is the simplest use of broadcast and the most satisfying
for young learners. A short scene with dialogue teaches sequencing, timing, and
coordination at once.

::: exercise
**Exercise 4.3 — Two-character scene**

1. Add two sprites.
2. Make them have a five-line conversation using `say` and `wait`.
3. Add a broadcast so the second character only begins after the first finishes.
4. Add a background that matches the scene.
5. Record it as a video and show it to someone.

**Time:** 40 minutes. **Deliverable:** a working scene.
:::

# Module 5 — Debugging: The Most Important Skill

## Lesson 5.1 — Bugs are normal

Every programmer, at every level, writes broken code constantly. The difference
between a beginner and an expert is not the number of bugs. It is the speed at
which they find them.

Teach children this explicitly, because the alternative — believing that good
programmers do not make mistakes — makes them quit at the first error.

## Lesson 5.2 — The four-step debugging method

1. **Reproduce it.** Make it happen again, deliberately.
2. **Narrow it.** Which block is the last one that worked correctly?
3. **Predict.** Say out loud what you think the next block does.
4. **Test one change at a time.** Never change three things and hope.

## Lesson 5.3 — Common beginner bugs

| Symptom | Usual cause |
|---|---|
| Nothing happens | The script is not connected to the green flag |
| It happens too fast | Missing `wait` blocks |
| It happens forever | `forever` loop with no exit condition |
| Score keeps rising | No reset at the start |
| Two scripts fight | Both control the same sprite's position |

::: exercise
**Exercise 5.3 — Break it on purpose**

1. Take your game from Module 3.
2. Deliberately introduce three bugs: remove the score reset, remove a wait,
   and add a forever loop with no exit.
3. Swap with a partner. Each finds the other's bugs.
4. Write down how you found each one.

**Time:** 30 minutes. **Deliverable:** three bugs found and explained.
:::

# Module 6 — Curriculum Alignment

## Lesson 6.1 — Mapping to the Uganda syllabus

The lower-secondary ICT curriculum in Uganda covers computational thinking,
algorithms, sequencing, and basic programming concepts. Scratch is the standard
vehicle for these, and this course covers each explicitly.

| Syllabus area | Where it is covered |
|---|---|
| Computational thinking | Module 1, Module 5 |
| Algorithms and sequence | Module 2 |
| Variables and logic | Module 3 |
| Events and coordination | Module 4 |
| Problem solving and debugging | Module 5 |

## Lesson 6.2 — Mapping to Cambridge

The Cambridge Primary and Lower Secondary Computing frameworks cover
computational thinking, programming, and managing projects. The same modules map
directly, with Module 7 providing the project work Cambridge assesses.

## Lesson 6.3 — For teachers: assessment evidence

Keep, for each learner: three saved projects (early, middle, final), a written
explanation of one program in their own words, and a debugging log. Those three
artefacts demonstrate every competency the syllabus requires.

::: exercise
**Exercise 6.3 — Teacher's evidence pack**

1. Create a folder structure for each learner.
2. Save their Module 2 shapes, Module 3 game, and Module 7 project.
3. Have each write a five-sentence explanation of how their game works.
4. Use the rubric in Module 8 to score.

**Time:** 45 minutes.
:::

# Module 7 — The Final Project

## Lesson 7.1 — Choose a project

Three project shapes that work well, in order of difficulty:

**The quiz game.** A question appears, the player chooses, the score changes.
Teaches conditionals, variables, and user input.

**The maze.** A character navigates walls to a goal. Teaches collision detection,
movement, and level design.

**The animated story.** Multiple scenes, dialogue, and music. Teaches sequencing,
broadcast, and timing.

Choose one. Build it over four sessions. Present it.

## Lesson 7.2 — The build plan

| Session | Goal |
|---|---|
| 1 | Design on paper: what happens, in what order |
| 2 | Build the core mechanic only |
| 3 | Add score, sound, and one level |
| 4 | Test with a classmate, fix, present |

Designing on paper first is not a delay. It is the difference between a project
that finishes and one that is abandoned in frustration.

::: exercise
**Exercise 7.2 — Paper first**

1. Draw your project on paper: every screen, every action.
2. Write the order of events.
3. List the sprites you need.
4. List the variables you need.
5. Only then open Scratch.

**Time:** 30 minutes.
:::

# Module 8 — Assessment and Presentation

## Lesson 8.1 — The rubric

| Criterion | Weight | Excellent | Developing |
|---|---|---|---|
| Works | 30% | Runs without help, handles a wrong answer | Crashes, needs rescue |
| Logic | 25% | Uses loops and conditionals appropriately | Long sequence, no loops |
| Design | 20% | Clear, readable, well laid out | Confusing, cluttered |
| Explanation | 15% | Explains the code in own words | Cannot explain |
| Persistence | 10% | Debugged independently | Gave up at first error |

## Lesson 8.2 — The presentation

Five minutes. Four things: what it does, how it works, the hardest bug, what they
would add next.

The third item is the one that reveals understanding. A child who can describe a
bug they fixed can program.

::: exercise
**Exercise 8.2 — Present**

1. Present in five minutes to the class.
2. Take two questions.
3. Watch two other presentations and give one specific compliment each.
4. Write one thing you would add if you had another week.

**Time:** 5 minutes per learner.
:::

# Module 9 — Where This Leads

::: scripture
"A man's gift makes room for him, and brings him before great men."
— Proverbs 18:11
:::

Scratch is not the destination. It is the door. From here:

- **Practical STEM** — robotics, where the same logic controls a physical machine.
- **Python** — the same concepts, typed instead of dragged. The step is smaller
  than it looks, because the thinking has already been learned.
- **AI Builder** — much later, for students who want to build the tools rather
  than use them.

The gift is the logic. Everything else is syntax, and syntax changes every few
years. The ability to break a problem into ordered steps will serve them for
fifty years.
