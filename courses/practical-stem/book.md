# Module 1 — Science With What You Have

A school science laboratory is a luxury. Curiosity is not. Every experiment in
this course can be built from materials available in any Ugandan market for less
than the cost of a textbook: wire, batteries, bulbs, bottles, seeds, string,
paper, water.

The purpose is not to memorise facts. It is to learn one habit: when something
surprises you, design an experiment rather than guessing.

::: scripture
"It is the glory of God to conceal a matter, but the glory of kings is to search
out a matter."
— Proverbs 25:2
:::

Searching out a matter. That is what science is, and it is presented in Scripture
as a royal activity. You do not need permission or equipment to think.

## Lesson 1.1 — The scientific method, plainly

Six steps. Nothing more.

1. **Observe** something that makes you curious.
2. **Ask** a question that can be answered by measurement.
3. **Predict** an answer — that is your hypothesis.
4. **Test** it with an experiment that could prove you wrong.
5. **Record** what actually happened.
6. **Conclude**, and ask the next question.

The critical point is step four: an experiment that cannot possibly prove you
wrong is not an experiment, it is a performance.

## Lesson 1.2 — Variables

Three words, and they make every difference.

**Independent variable** — what you change deliberately.
**Dependent variable** — what you measure.
**Controlled variables** — everything else you keep the same.

The classic error: changing two things and concluding which one mattered. If you
water the plant more *and* move it to the sun, you have learned nothing.

## Lesson 1.3 — Recording honestly

A record includes: the date, what you changed, what you measured, the actual
numbers, and anything unusual that happened.

Write down the results you did not want. That is not cheating avoided; it is
science performed.

::: exercise
**Exercise 1.3 — Your first investigation**

Question: does a paper cup of water cool faster with a lid or without?

1. Two identical cups, same amount of hot water, same starting temperature.
2. One with a lid, one without. Same room, same place.
3. Measure the temperature every three minutes for fifteen minutes.
4. Record in a table.
5. Plot the two lines on one graph.

**Time:** 40 minutes. **Deliverable:** a table, a graph, and one conclusion.
:::

# Module 2 — Electricity and Circuits

## Lesson 2.1 — What electricity is, practically

Electricity is the movement of charge through a conductor. In a circuit, charge
flows from one terminal of a battery, through a component, and back to the other
terminal.

A circuit must be a complete loop. Break the loop anywhere, and the current stops.
That one sentence explains half of all electrical problems you will ever meet.

## Lesson 2.2 — The series circuit

Components one after another, in a single loop.

- If one bulb breaks, all go out.
- Adding bulbs makes all of them dimmer.
- Current is the same everywhere.

## Lesson 2.3 — The parallel circuit

Components on separate branches.

- If one bulb breaks, the others stay on.
- Adding branches does not dim the others.
- This is how your house is wired, and why one broken bulb does not darken the
  house.

## Lesson 2.4 — The materials list

| Item | Source | Cost |
|---|---|---|
| 1.5V batteries | Any shop | Cheap |
| Bulb and holder | Electronics shop | Cheap |
| Insulated wire | Electronics shop | Cheap |
| Paper clips, coins, pencils | Home | Free |
| Salt, lemon, potato | Market | Free |

The conductivity test is the classic first experiment: build a circuit with a gap,
then place different materials in the gap and see whether the bulb lights. Copper
and salt water conduct; plastic and wood do not.

::: warn
**Safety.** Use only 1.5V and 3V batteries. Never experiment with mains electricity.
Never short a battery directly for long periods — it heats and can leak or burn.
:::

::: exercise
**Exercise 2.4 — Series versus parallel**

1. Build a series circuit with two bulbs. Remove one. Record what happens.
2. Build a parallel circuit with two bulbs. Remove one. Record what happens.
3. Measure brightness subjectively (very bright, bright, dim, off) in both.
4. Write one sentence explaining the difference.

**Time:** 45 minutes. **Deliverable:** two circuits and a written comparison.
:::

# Module 3 — Magnetism and Motors

## Lesson 3.1 — Magnets

A magnet has two poles. Like poles repel; opposite poles attract. The field is
strongest at the poles. Iron, nickel and cobalt are attracted; copper and plastic
are not.

## Lesson 3.2 — Electromagnets

Wrap wire around an iron nail, connect a battery, and you have an electromagnet.
More turns of wire, or more current, produces a stronger field. This is the
principle inside every motor, speaker and doorbell.

## Lesson 3.3 — The simple motor

A coil of wire, a magnet, and a battery. When current flows through the coil in a
magnetic field, the coil is pushed — and it turns.

This is not a demonstration of a curiosity. It is the same principle that runs
fans, water pumps, and every electric vehicle. A learner who builds one has held
the idea in their hand.

::: exercise
**Exercise 3.3 — Build an electromagnet**

1. Wrap 30 turns of insulated wire around an iron nail.
2. Connect to a battery. Test what it picks up (paper clips).
3. Increase to 60 turns. Test again. Record the difference.
4. Try a second battery in series. Record the difference.
5. Write the rule: what increases the strength?

**Time:** 40 minutes. **Deliverable:** an electromagnet and a written rule.
:::

# Module 4 — Measurement and Data

## Lesson 4.1 — Measuring properly

Every measurement has a unit and an uncertainty. "The table is 120" means nothing.
"The table is 120 cm, plus or minus 1 cm" is a measurement.

Read at eye level. Measure twice. Record the unit every time.

## Lesson 4.2 — From table to graph

A table is a record. A graph is an argument. The graph should make one thing
visible immediately.

Rules: label both axes with units, choose a sensible scale, plot the points, draw
the line of best fit, give it a title that states what it shows.

## Lesson 4.3 — Interpreting honestly

Three questions of any graph:

1. What is the trend?
2. Is there a point that does not fit — and why?
3. Does the trend continue, or does it level off?

That third question is where most school science stops and real science begins.

::: exercise
**Exercise 4.3 — Measure and plot**

1. Measure the height of ten classmates, to the nearest centimetre.
2. Tabulate.
3. Plot a bar chart of the individual values.
4. Calculate the average.
5. Write two sentences: what does the distribution look like, and why?

**Time:** 45 minutes. **Deliverable:** a table, a chart, and two sentences.
:::

# Module 5 — Introductory Robotics

## Lesson 5.1 — A robot is three things

**Sensors** — how it knows about the world.
**A controller** — how it decides.
**Actuators** — how it acts.

That is the whole architecture, whether the robot is a block kit or a
self-driving car. Once a learner sees these three parts, they can look at any
machine and understand it.

## Lesson 5.2 — Block-based robot programming

Most educational kits use the same block logic as Scratch: sequence, loops,
conditionals, sensors as inputs.

The first program: move forward, detect an obstacle, stop, turn, continue.

```
forever
  if <distance sensor < 20cm> then
    stop
    turn right 90 degrees
  else
    move forward
```

A robot that avoids walls. Twenty lines. And the learner has implemented the
control loop that runs inside every vacuum cleaner and every warehouse vehicle.

## Lesson 5.3 — The engineering habit

Build, test, break, improve. A robot that works on the first attempt has taught
nothing. The value is in the iteration, and the iteration requires recording what
you changed.

::: exercise
**Exercise 5.3 — The obstacle course**

1. Build a simple course from books or boxes.
2. Program a robot to traverse it.
3. Time each attempt. Record the changes you make between attempts.
4. Aim for three consecutive clean runs.
5. Present your final program and explain what you changed.

**Time:** 90 minutes. **Deliverable:** a working program and a change log.
:::

# Module 6 — Maths Modelling With Real Data

## Lesson 6.1 — Why model

A model lets you predict without testing everything. If you know how fast a
bicycle travels, you can predict arrival times without riding every route.

## Lesson 6.2 — Building a simple model

Measure something. Find the relationship. Write it as an equation. Use the
equation to predict. Test the prediction.

Example: measure the circumference of five circles and their diameters. Plot one
against the other. The gradient is roughly 3.14. You have just derived pi
experimentally, which is more instructive than being told it.

## Lesson 6.3 — When models fail

A model is only valid within the range you tested. A model of plant growth over
two weeks does not predict two years. State the limits of your model; this is a
habit that separates a scientist from someone who has memorised a formula.

::: exercise
**Exercise 6.3 — Derive pi**

1. Find five circular objects of different sizes.
2. Measure circumference (string, then ruler) and diameter.
3. Tabulate and plot.
4. Calculate circumference ÷ diameter for each.
5. Write the average and compare to 3.14159. Explain the difference.

**Time:** 45 minutes. **Deliverable:** a derivation with a graph.
:::

# Module 7 — The Science Poster

## Lesson 7.1 — Structure

A poster has six parts, in this order: question, method, results, graph,
conclusion, next question.

It is the same structure as a scientific paper, compressed. Learning it now means
that writing a report later is not a new skill.

## Lesson 7.2 — Design that communicates

Big title, readable from two metres. One graph, large. Three colours maximum.
Short sentences. No paragraphs of prose — nobody reads them at a poster session.

## Lesson 7.3 — Presenting

Two minutes. What you asked, what you did, what you found, what surprised you.
The last one is what makes a presentation memorable.

::: exercise
**Exercise 7.3 — Make the poster**

1. Choose your best experiment from this course.
2. Build the poster with the six sections.
3. Design it in Canva if available.
4. Present in two minutes to the group.
5. Answer one question you did not prepare for.

**Time:** 60 minutes. **Deliverable:** a printed or displayed poster.
:::

# Module 8 — Capstone: An Independent Investigation

## Lesson 8.1 — The brief

Choose your own question. Design the experiment. Control the variables. Collect
real data. Present the finding.

Suggested questions that work with local materials:

- Does the colour of a container affect how fast water cools?
- Does the amount of salt affect how long a candle burns?
- Which local material insulates best?
- Does music affect how quickly someone completes a simple task?
- Does the angle of a solar panel affect its output?

## Lesson 8.2 — The rubric

| Criterion | Weight | Excellent | Weak |
|---|---|---|---|
| Question | 15% | Testable, specific, original | Vague, unanswerable |
| Method | 25% | Variables controlled, repeatable | Two things changed at once |
| Data | 25% | Real measurements, honest recording | Invented or incomplete |
| Analysis | 20% | Graph supports a specific conclusion | Graph with no interpretation |
| Presentation | 15% | Clear, honest, answers questions | Reads from the page |

::: scripture
"Great are the works of the Lord, studied by all who delight in them."
— Psalm 111:2
:::

Studied by all who delight in them. Science is not a subject for a select group
of clever people. It is what happens when anyone pays close enough attention to
something to be surprised by it.

::: prayer
**A closing reflection**

Lord, give me eyes that notice, patience to measure carefully, and honesty to
record what I actually saw rather than what I expected. Let curiosity be a form
of worship.
Amen.
:::
