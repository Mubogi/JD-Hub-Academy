# Module 1 — From User to Operator

You can already get good answers out of an AI tool. That is not the skill this
tier teaches. This tier teaches you to build *systems* — repeatable processes
that produce the same quality whether you are in the room or not, whether you
are tired or fresh, whether it is you doing it or a colleague you trained
yesterday.

The difference between a user and an operator is the difference between a person
who can cook a good meal and a person who can run a kitchen.

::: scripture
"Whatever your hand finds to do, do it with your might."
— Ecclesiastes 9:10
:::

Half-hearted systems fail quietly. A prompt library nobody uses, a workflow
documented only in your head, a bot that answers three questions well and
invents answers to the rest. This tier is about doing the work with your might —
which means building things that hold up when you are not watching.

## Lesson 1.1 — Why ad-hoc prompting does not scale

Three people on the same team, using the same AI tool, will produce three
different quality levels. Not because the tool is inconsistent, but because each
person is improvising. Improvisation is fine for one person. It is expensive for
five.

The symptoms of ad-hoc AI use:

- Quality depends on who is working that day.
- Nobody can explain why one output was good and another was bad.
- Every new staff member starts from zero.
- There is no way to audit what was generated, by whom, with what instructions.
- When the tool changes, everyone's output degrades at once.

The cure is unglamorous: write it down, test it, reuse it.

## Lesson 1.2 — The three artefacts of an operator

Every mature AI operation has three things. Build these three and you have moved
from user to operator.

**1. A prompt library.** A shared document, one prompt per task, each with a
title, the task it solves, the prompt itself, an example output, and notes on
what to check. Not a folder of screenshots. A working document people actually
open.

**2. A workflow map.** For each recurring process, a one-page diagram: inputs,
which tool does what, where the human checks, what the output is, who owns it.

**3. A quality checklist.** The specific things a human must verify before the
output leaves the building. Different for a social caption and a quotation.

## Lesson 1.3 — The economics that justify this

Operators get asked to justify the effort. Here is the arithmetic.

If a task takes 40 minutes by hand and 12 minutes with AI plus 5 minutes of
checking, you save 23 minutes. Do it twice a week and that is 46 minutes a week,
roughly 37 hours a year. If four people do that task, you have recovered 148
hours — nearly four working weeks.

Now the part people forget: without a shared prompt library, only the person who
figured it out gets those savings. With one, the whole team does. That is why
the library is the highest-return artefact in this course.

::: exercise
**Exercise 1.3 — Audit your own week**

1. List every recurring task in your week that involves producing or reshaping text.
2. For each, write: minutes by hand, minutes with AI (honestly), and how often
   per month.
3. Multiply out the annual hours saved.
4. Circle the three with the biggest numbers.

**Time:** 25 minutes. **Deliverable:** the table. You will build your library
from the three circled tasks.
:::

# Module 2 — Prompt Architecture

A prompt is not a sentence. It is a specification. This module treats it like
one: with structure, with variables, with tests, and with a version history.

## Lesson 2.1 — Anatomy of a production prompt

A production prompt has more parts than a chat prompt, because it must work
without you standing over it.

| Part | Purpose | Example |
|---|---|---|
| **Role** | Sets vocabulary and assumptions | "You are a grants writer for small NGOs" |
| **Task** | The single job | "Draft a two-page concept note" |
| **Inputs** | Named variables to fill | `{organisation}`, `{donor}`, `{budget}` |
| **Constraints** | Hard rules | "Never exceed 700 words. No invented statistics." |
| **Format** | Exact output shape | "Headings: Problem, Approach, Budget, Risk" |
| **Examples** | One good output to match | A previous note you liked |
| **Self-check** | Forces verification | "List any figure you could not source" |

The two parts beginners never include are **Examples** and **Self-check**. They
are the two that most improve reliability.

## Lesson 2.2 — Variables and templates

When a prompt will be reused, make the changing parts obvious. Use curly braces
and a legend.

```prompt
You are a procurement officer for {organisation}.

Draft a request for quotation for {item_description}, quantity {qty},
delivery to {location} by {deadline}.

Constraints:
- Include a submission deadline and a validity period of 30 days.
- Require the supplier to state VAT registration status.
- Do not invent a budget figure; leave it as [BUDGET].

Format: a one-page letter, with a table for the item specification.

After the letter, list every assumption you made.
```

Anyone on the team can now produce a correct RFQ. Nobody has to remember the VAT
line, because the prompt remembers it.

## Lesson 2.3 — Testing a prompt

You would not deploy a form without testing it. Do not deploy a prompt without
testing it either.

The minimum test: run it five times on five different real inputs and read all
five outputs. Look for:

- **Drift** — does the format change between runs?
- **Edge-case failure** — what happens with an unusually long input, a missing
  field, or a very short one?
- **Silent invention** — does it fill gaps with plausible fiction?
- **Tone inconsistency** — does it sound like the same organisation each time?

Write the results into the prompt's notes. "Fails on inputs over 800 words —
splits the table badly." That note saves a colleague an hour next month.

## Lesson 2.4 — Prompt chains

Complex work rarely fits one prompt. A chain breaks it into stages you can
inspect separately.

The three-stage pattern that works for almost everything:

1. **Extract** — pull the relevant facts out of the material.
2. **Decide** — choose an approach, given the facts.
3. **Produce** — write the final output, given the decision.

Example: writing a proposal.

```prompt
Stage 1 — From the donor guidelines below, extract: eligibility criteria,
required sections, word limits, and every deadline. Quote the source
sentence for each.
```

```prompt
Stage 2 — Given those requirements and our project summary, propose the
strongest angle for this proposal in five bullets. Name the one weakness in
our fit and how we should address it.
```

```prompt
Stage 3 — Write the concept note following the extracted structure exactly.
Do not exceed the word limits. Mark any claim needing a source as [VERIFY].
```

The `[VERIFY]` marker is the most valuable habit in this module. It turns a
hidden risk into a visible task list.

::: exercise
**Exercise 2.4 — Build a three-stage chain**

1. Choose a recurring document you produce.
2. Write the three stages: extract, decide, produce.
3. Run it on a real case.
4. Add a `[VERIFY]` marker rule.
5. Save all three prompts in your library under one title.

**Time:** 45 minutes. **Deliverable:** a working chain, saved.
:::

# Module 3 — The Shared Prompt Library

This is the module that turns individual skill into organisational capability.
It is boring. It is also the highest-return thing in this course.

## Lesson 3.1 — Structure that survives contact with staff

A library nobody uses is a document that got written once. To survive, it needs
four properties.

**Findable.** Organised by *task*, not by tool. Nobody wakes up wanting "a
ChatGPT prompt". They want "reply to an angry customer".

**Copyable.** The prompt sits in a code block so one tap copies it. Not
screenshots. Not a PDF.

**Tested.** Each entry says when it was last tested and by whom.

**Owned.** Each entry has a named owner who fixes it when it breaks.

## Lesson 3.2 — The entry template

Every entry uses the same seven fields.

::: box
**TITLE** — Reply to a complaint about late delivery

**WHEN TO USE** — A customer complains that an order arrived late and wants a
refund.

**PROMPT**
```
You are a customer service manager for {business}, which sells {products}
with a stated delivery window of {days} days.

A customer has complained that their order arrived {actual_days} days late
and is asking for a refund.

Write a reply that: apologises specifically for the delay (not generically),
explains what happened in one sentence without excuses, offers {remedy},
and ends with a clear next step. Maximum 120 words. Do not promise anything
not listed in the remedy.
```

**EXAMPLE OUTPUT** — one real, approved example.

**WHAT TO CHECK** — That the remedy offered is one we actually authorise.
That no delivery date is promised that operations cannot meet.

**OWNER** — Customer service lead. Last tested: March 2026.
:::

Notice what the "what to check" field does. It encodes a judgement that would
otherwise live only in one person's head.

## Lesson 3.3 — Getting people to actually use it

The library fails for social reasons, not technical ones. Three interventions
that work:

1. **Build it with them, not for them.** Run a session where each person
   contributes one prompt. Authors use what they wrote.
2. **Make the first five entries obviously useful.** The five most-resented
   tasks in the organisation. Nothing abstract.
3. **Review it monthly, for ten minutes.** Delete what nobody used. Add what
   people asked for. A living document of twenty prompts beats a dead one of two
   hundred.

::: exercise
**Exercise 3.3 — Seed the library**

1. Create a shared document.
2. Add five entries using the seven-field template, from your own work.
3. Share it with two colleagues and ask each to add one.
4. Book a ten-minute monthly review in the calendar, now.

**Time:** 60 minutes. **Deliverable:** a shared document with seven entries and
a recurring calendar invite.
:::

# Module 4 — Document Intelligence

Most organisational knowledge is trapped in documents nobody has time to read.
This module gets it out.

## Lesson 4.1 — Grounded question answering

Tools like NotebookLM and grounded assistants answer *only* from the documents
you give them. That constraint is the feature: the answer is traceable to a
page.

The workflow for any document set — policies, tenders, contracts, reports:

```prompt
Based only on the uploaded documents:
1. Summarise the main argument in five bullets.
2. List every figure, with the document and section it came from.
3. List every obligation placed on us, with a deadline if stated.
4. Identify contradictions between documents.
5. Tell me what is NOT covered that I should ask about.
```

Item 3 earns its keep in procurement and compliance. Item 5 earns its keep in
meetings.

## Lesson 4.2 — The contradiction hunt

When you upload several documents, contradictions are common and almost never
noticed by humans reading sequentially. Versions of a policy disagree. A budget
line in the narrative does not match the spreadsheet.

Ask directly: *"Where do these documents contradict each other? Quote both
sentences."* Then verify both quotes exist. This is a fifteen-minute task that
used to take a day.

## Lesson 4.3 — When to trust the summary

A summary is a compression, and compression loses things. Trust it when you need
orientation. Do not trust it when:

- Money, liability, or deadlines depend on the detail.
- The question is whether the document *said* X — that requires the exact text.
- You are signing something.

The habit: use the summary to find the page, then read the page.

::: exercise
**Exercise 4.3 — Contract interrogation**

1. Take any contract or policy you have signed.
2. Run the five-part prompt above.
3. Verify every figure against the document.
4. Find one obligation you had forgotten about.

**Time:** 30 minutes. **Deliverable:** a one-page summary you would be
comfortable forwarding to your board.
:::

# Module 5 — The Content Engine at Team Scale

The Foundation tier taught one person to produce a week of content. This module
makes that a team process with a calendar, an approval step, and a measurement.

## Lesson 5.1 — The pipeline

**Ideas → Brief → Draft → Approve → Schedule → Measure.**

The failure mode in small teams is skipping Brief and Approve. Without a brief,
drafts are generic. Without approval, something inaccurate or off-brand goes out
and nobody knows who to blame.

## Lesson 5.2 — The brief that makes drafting easy

One paragraph per post. If the brief is good, the draft takes two minutes. If the
brief is vague, the draft takes twenty and is still wrong.

::: box
**BRIEF — Post 3 of 7, week 14**

Audience: parents of primary-school children in Kampala.
Goal: 20 bookings for the holiday programme.
Angle: what a child actually does in a day with us.
Proof: photos from last holiday, one parent quote.
Call to action: WhatsApp "HOLIDAY" to 07xx.
Tone: warm, concrete, no hype.
Do not: use the word "fun" more than once.
:::

## Lesson 5.3 — Measuring without vanity

Two numbers matter per post: did the right people see it, and did anyone act?
Impressions without action is decoration.

Track per week: reach, saves or shares, and enquiries attributed. Three numbers,
one row, five minutes on a Friday. After eight weeks you will know which angle
produces customers — and it is almost never the one you would have guessed.

::: exercise
**Exercise 5.3 — Run one full cycle**

1. Write briefs for three posts.
2. Have someone else draft them from the briefs alone — this tests the brief.
3. Approve, schedule, publish.
4. Record the three numbers for each after seven days.
5. Write one sentence: what would you change next week?

**Time:** 60 minutes plus a week of measurement.
**Deliverable:** a completed row of the tracker.
:::

# Module 6 — Automation That Actually Runs

The Foundation tier taught one automation. This module teaches you to design
automations that survive, and to know which ones to refuse.

## Lesson 6.1 — The reliability test

Before building, ask four questions.

1. **What happens when it fails?** Every automation fails eventually. If failure
   is silent, you have built a trap.
2. **Who notices?** There must be a named person who sees the failure.
3. **Can it be undone?** Reversible automations are safe to try. Irreversible
   ones need approval gates.
4. **What is the cost of a false positive?** A confirmation sent to the wrong
   person is embarrassing. A payment sent to the wrong person is not.

## Lesson 6.2 — Patterns worth building

| Pattern | Example | Why it works |
|---|---|---|
| **Capture** | Form → sheet → confirmation email | Nothing lost, customer reassured |
| **Digest** | Daily summary of new enquiries to one person | One message replaces twenty checks |
| **Nudge** | Invoice unpaid after 7 days → reminder draft | Consistency without nagging manually |
| **Route** | Enquiry keyword → correct staff member | Response time falls sharply |
| **Publish** | Approved draft → scheduled post | Removes the last manual step |

## Lesson 6.3 — Patterns to refuse

Do not automate refunds, disciplinary communication, medical or legal advice,
anything committing money without human approval, or anything where the recipient
would feel deceived if they knew a machine did it.

::: warn
**The deception line.** Automating *effort* is fine. Automating the *appearance
of personal attention* is not. A templated birthday message is fine. A machine
pretending to be a named staff member in a sensitive conversation is not.
:::

::: exercise
**Exercise 6.3 — Design and stress-test**

1. Choose one pattern from the table.
2. Answer the four reliability questions in writing.
3. Build it.
4. Deliberately break it: a blank form, a duplicate, a nonsense entry.
5. Fix what broke, then document who notices failures.

**Time:** 60 minutes. **Deliverable:** a running automation plus a one-page
failure plan.
:::

# Module 7 — Measurement and Reporting

If you cannot show the number, you cannot defend the budget. This module is about
proving the value of what you built.

## Lesson 7.1 — What to measure

Three levels, in increasing order of persuasiveness.

**Activity** — how many times the tool was used. Weak on its own.

**Time** — minutes saved per task, multiplied by frequency. Good, if measured
honestly rather than estimated.

**Outcome** — response time to enquiries, quotes issued per week, content
published per month, error rate on invoices. Strongest, because it is what the
organisation actually cares about.

## Lesson 7.2 — Measuring time honestly

The temptation is to estimate generously. Resist it, because a number that
collapses under questioning destroys your credibility for everything else.

Method: time the old way three times with a stopwatch. Time the new way three
times, including checking. Average both. Report the difference and the method.
Anyone can attack an estimate; almost nobody attacks a method.

## Lesson 7.3 — The one-page report

::: box
**AI WORKFLOW REPORT — Q1**

**What we built.** Reply bank (WhatsApp), quotation generator, weekly content
pipeline.

**Time saved.** Quotations: 38 min → 11 min, 60 per month → 27 hours per month.
Content: 6 hours per week → 90 minutes per week.

**Outcome.** Enquiry response time 9 hours → 40 minutes. Quotes issued up 22%.

**What went wrong.** Two quotations had a wrong total in week three — the AI
computed instead of referencing the sheet. Fixed by removing arithmetic from the
prompt and referencing the spreadsheet only.

**What is next.** Proposal chain, and a shared prompt library for the sales team.
:::

That "what went wrong" paragraph is what makes the report credible. A report
with no failures reads as marketing.

::: exercise
**Exercise 7.3 — Write your report**

1. Time one task the old way, three runs.
2. Time it the new way, three runs, including checking.
3. Write the one-page report above, with one honest failure.
4. Have someone who does not trust AI read it and try to pick holes.

**Time:** 45 minutes. **Deliverable:** a one-page report that survives scrutiny.
:::

# Module 8 — Training Your Colleagues

The last skill of an operator is multiplication. If only you can do it, you are a
bottleneck, not a capability.

## Lesson 8.1 — Three kinds of learner

Never train a mixed room the same way.

**The frightened** believe they will break something or be replaced. They need
safety first: what not to do, and the assurance that judgement is still theirs.

**The curious** will experiment and get good results but inconsistently. They
need structure: R-T-C-F, the follow-up moves, the library.

**The impatient** want the shortcut. They need one task, done live, that saves
them an hour this week. Nothing else will hold their attention.

## Lesson 8.2 — The 45-minute session format

1. **Ten minutes:** one live demo on a task the room recognises. No slides.
2. **Twenty minutes:** everyone does the same task on their own work. You roam.
3. **Ten minutes:** two people show their screens. Critique the *prompt*, not
   the person.
4. **Five minutes:** one sentence each — "tomorrow I will…"

That format works for almost any audience and any tool.

## Lesson 8.3 — What to tell people who are afraid

Say it plainly, in this order:

1. Your judgement is the product. The tool produces drafts.
2. The people who will struggle are not those who use AI badly, but those who
   refuse to check it.
3. Here is exactly what you must never paste in. (Then the list.)
4. Here is the one task I want you to try this week. (One task, not five.)

::: scripture
"And let us consider one another in order to stir up love and good works."
— Hebrews 10:24
:::

Training is a form of consideration for others. You are not showing off what you
learned; you are removing a burden from someone's week.

::: exercise
**Exercise 8.3 — Deliver one session**

1. Pick one colleague and one task.
2. Run the 45-minute format with them.
3. Watch where they get stuck — that is your library's next entry.
4. Ask them, one week later, whether they are still using it.

**Time:** 45 minutes plus follow-up. **Deliverable:** one colleague who can do
the task without you.
:::

# Module 9 — Capstone: A Department-Level System

Build something that outlives your involvement. This is the difference between
this tier and the last.

## Lesson 9.1 — The brief

Deliver a working system with: a prompt library of at least ten entries, one
documented workflow, one automation, one measured outcome, and one colleague
trained to run it without you.

## Lesson 9.2 — The rubric

| Criterion | Weight | Excellent | Weak |
|---|---|---|---|
| Library quality | 25% | Ten tested entries another person could use unaided | Screenshots or untested prompts |
| Measured outcome | 25% | Honest method, credible number | Estimate with no method |
| Transfer | 25% | A colleague runs it live, unaided | Only the author can operate it |
| Risk handling | 15% | Named failure modes and owners | No failure plan |
| Documentation | 10% | One page, readable in five minutes | Forty pages nobody reads |

## Lesson 9.3 — Presenting to management

Four sentences, in this order:

1. What it does, in the language of the business, not the technology.
2. What it saves, with the number and the method.
3. What could go wrong, and who watches it.
4. What you want next — a decision, not a demo.

::: exercise
**Exercise 9.3 — Ship the system**

1. Build all five components.
2. Have your trained colleague run it while you watch and say nothing.
3. Fix whatever they stumble on. That is the real deliverable.
4. Present in four sentences.

**Time:** 90 minutes. **Deliverable:** a system that runs without you.
:::

# Module 10 — Where to Go Next

::: scripture
"Plans fail for lack of counsel, but with many advisers they succeed."
— Proverbs 15:22
:::

The next tier, **AI-301 Builder**, is for people who want to build the tools
rather than use them: custom assistants grounded in your own documents,
brand-locked image systems, voice and video production, and agents that take
actions.

The tier after that, **AI-401 Specialist**, is for people who want to sell and
govern this work: policy, evaluation, procurement and consulting.

Take the next tier when you have shipped something in this one. Not before. A
certificate without a shipped system is a piece of paper; a shipped system is a
reputation.
