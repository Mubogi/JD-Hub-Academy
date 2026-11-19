# Module 1 — What Changes at Builder Level

At Practitioner level you made yourself and your team faster. At Builder level
you make something that other people use without you. The output is no longer a
document — it is a tool.

This is a real shift in responsibility. A bad prompt wastes ten minutes. A bad
bot that a customer relies on damages a reputation. The Builder tier is therefore
as much about restraint and testing as it is about capability.

::: scripture
"Suppose one of you wants to build a tower. Won't you first sit down and
estimate the cost to see if you have enough money to complete it?"
— Luke 14:28
:::

Count the cost before you build. Most failed AI projects in small organisations
fail at this point: somebody built something impressive that nobody maintained.

## Lesson 1.1 — The four things you will build

**1. A grounded assistant.** A chat interface trained on your organisation's own
documents, so it answers in your policies, your prices, your voice — and refuses
to answer outside them.

**2. An image system.** A repeatable way to produce on-brand visuals, so that
every poster, thumbnail and social graphic looks like it came from the same
organisation.

**3. A media pipeline.** Voice, video, captions and repurposing, produced at a
volume one person could not previously manage.

**4. An agent.** Something that takes actions — books, files, notifies, drafts
and sends — with guardrails.

## Lesson 1.2 — The builder's rule: grounding beats cleverness

A spectacular prompt on an ungrounded model will still invent your prices. A
plain prompt on a well-grounded model will quote them correctly.

Grounding means: giving the model the actual source material and instructing it
to answer only from that material. Everything else in this tier is secondary.

::: warn
**The confident-gap problem.** Ungrounded assistants do not say "I don't know".
They answer, plausibly, and wrongly. A customer-facing assistant without
grounding is a liability with a friendly face.
:::

## Lesson 1.3 — What you need before you start

- A folder of clean source documents. Policies, price list, FAQ, service
  descriptions. If these are inconsistent, fix them first — you are about to
  automate the inconsistency.
- A named owner for the finished tool. Not "the team". A person.
- An escalation path. What happens when the tool cannot answer.
- A test set. Twenty real questions with correct answers, written down before
  you build, so you can measure whether it works.

That last item is the one people skip and regret.

::: exercise
**Exercise 1.3 — Assemble the source pack**

1. Create a folder called `source-pack`.
2. Add: your price list, your FAQ, your service descriptions, your refund or
   delivery policy, and any standard terms.
3. Read them for contradictions. Fix at least one.
4. Write twenty real questions your customers ask, with the correct answer
   beside each.

**Time:** 60 minutes. **Deliverable:** a clean source pack and a twenty-question
test set. You will use both in Module 2.
:::

# Module 2 — Grounded Assistants

## Lesson 2.1 — The build, step by step

Tools such as custom GPTs, Gemini Gems, and Chatbase all follow the same logic:
give the model instructions and knowledge, then constrain it.

The build sequence that works:

1. **Upload the source pack.** Not the whole website. The specific documents.
2. **Write the instruction block** (below).
3. **Set the refusal behaviour** explicitly.
4. **Run the twenty-question test set.** Score it.
5. **Fix, re-run.** Repeat until at least eighteen of twenty are correct.

## Lesson 2.2 — The instruction block

```prompt
You are the customer assistant for {organisation}, which {what you do}
in {location}.

YOUR KNOWLEDGE
Answer only from the uploaded documents. They are the single source of truth
for prices, policies, delivery times and availability.

HARD RULES
- Never state a price that is not written in the documents.
- Never promise a delivery date. Quote the delivery window only.
- Never discuss competitors, give legal or medical advice, or offer a discount.
- If the answer is not in the documents, say: "I don't have that information —
  let me connect you with a member of our team," and stop.

STYLE
Friendly, brief, no more than three sentences unless the customer asks for
detail. Use the customer's language if they write in another language.

ALWAYS END WITH
One clear next step: a phone number, a link, or an offer to hand over.
```

Every line in that block is a decision you made deliberately. That is what
separates a builder from someone who typed "be helpful".

## Lesson 2.3 — Scoring the test set

Score each of the twenty questions: correct, partially correct, or wrong. Then
look at the wrong ones and ask why.

| Failure type | Fix |
|---|---|
| Answered from outside the documents | Strengthen the grounding instruction |
| Invented a price | Add the price list explicitly; add a hard rule |
| Over-answered a simple question | Add a length constraint |
| Refused something it should answer | The document is missing or badly formatted |
| Wrong tone | Add two example exchanges |

A pass is eighteen of twenty. Anything less is not ready for a customer.

::: exercise
**Exercise 2.3 — Build and score**

1. Build the assistant using the instruction block.
2. Run all twenty test questions. Record the score.
3. Fix the top three failures.
4. Re-run. Record the new score.
5. Write down the remaining two failures and decide whether they are acceptable.

**Time:** 75 minutes. **Deliverable:** a scored test sheet showing improvement.
:::

# Module 3 — Retrieval: When the Documents Are Too Many

## Lesson 3.1 — The limit of pasting

Pasting documents works until you have forty of them or a document longer than a
book. Then you need retrieval: the system finds the relevant passages and gives
only those to the model.

You do not need to build this from scratch. Most platforms now offer it: upload a
knowledge base, and the tool retrieves relevant chunks per question.

## Lesson 3.2 — What makes retrieval fail

Retrieval fails for mundane reasons, and all of them are fixable.

**Bad chunking.** A table split across two chunks answers neither question
properly. Fix: keep tables intact, one per section.

**Duplicate documents.** Two versions of the price list means the model picks
either. Fix: one canonical document, dated.

**Unstructured text.** A policy written as three pages of prose retrieves badly.
Fix: rewrite with headings and short paragraphs.

**No metadata.** If every chunk looks alike, retrieval cannot tell the refund
policy from the delivery policy. Fix: clear headings, one topic per section.

## Lesson 3.3 — Testing retrieval specifically

Ask questions whose answers live in one specific section, and check whether the
answer cites that section. Then ask a question whose answer is spread across two
documents — this is where retrieval usually fails and where you will need to
restructure.

::: exercise
**Exercise 3.3 — Break your retrieval**

1. Ask five questions whose answers sit in one short section.
2. Ask three questions that need two documents combined.
3. Note which failed.
4. Restructure the documents to fix the two most common failures.
5. Re-test.

**Time:** 45 minutes. **Deliverable:** a document set that retrieves reliably.
:::

# Module 4 — The Brand-Locked Image System

AI image generation is now genuinely capable: product scenes, editorial
illustrations, backgrounds, patterns, mock-ups. The problem is consistency.
Anyone can generate one striking image. Very few can generate forty that look
like they belong together.

## Lesson 4.1 — Why consistency is the whole job

A brand is recognisable before it is read. If every post uses a different visual
style, the audience never learns to recognise you, and recognition is what makes
marketing compound.

The system, therefore, is not "generate images". It is "generate images that
match this specification, every time".

## Lesson 4.2 — The style specification

Write this once, then paste it into every image prompt.

::: box
**BRAND IMAGE SPEC — JD Hub Academy**

Palette: midnight navy #060b18 ground, gold #e3a821 and #ffd166 accents,
cobalt #1d4fd6 for secondary elements. Never more than three colours.

Light: warm, directional, from upper left. Soft shadows. No harsh flash.

Mood: calm, competent, optimistic. Never frantic or gaudy.

Composition: subject off-centre, generous negative space on one side for text.
Nothing important in the bottom 15 percent.

Texture: subtle film grain. No glossy plastic sheen.

Avoid: stock-photo smiling, lens flare, floating holograms, generic "AI look",
text in the image, more than two people.
:::

Now every prompt begins with "Follow this specification: …" and ends with the
subject. The output becomes recognisably yours.

## Lesson 4.3 — The four jobs images actually do

| Job | Use | Example prompt shape |
|---|---|---|
| **Background** | Behind text on a poster | "Abstract geometric pattern, navy and gold, low contrast, space for text" |
| **Illustration** | Explaining a concept | "Flat vector illustration of a person organising papers into three piles" |
| **Scene** | Setting a mood | "A market stall at dawn, warm light, photographic, shallow depth of field" |
| **Mock-up** | Showing a product | "A phone on a wooden desk displaying a blank screen, soft daylight" |

For product photography, photograph the real product and use AI for the
background. Generated products mislead customers and, in most jurisdictions,
breach consumer-protection rules.

## Lesson 4.4 — The rejection habit

Generate six. Keep one. Delete five. The people whose AI images look bad are the
people who keep the first output because it took effort to make.

Set a rule: you may not use the first generation. Ever. This single rule raises
output quality more than any prompt technique.

::: exercise
**Exercise 4.4 — Build your spec and prove consistency**

1. Write your own brand image specification using the template.
2. Generate six images for one subject using the spec.
3. Keep one, delete five.
4. Generate three more different subjects using the same spec.
5. Put all four side by side. Do they look like one family?

**Time:** 50 minutes. **Deliverable:** a written spec and four consistent images.
:::

# Module 5 — Voice and Video Production

## Lesson 5.1 — Voiceover

Synthetic voice is now good enough for internal training, explainer videos, and
many advertisements. It is not good enough to impersonate a real person, and you
should not try — that is both unethical and, in a growing number of places,
illegal.

The production rules:

- Write for the ear, not the eye. Short sentences. One idea each.
- Punctuate for pace. A full stop is a pause; a comma is a breath.
- Generate at a slower speed than feels right, then speed up 5 percent in editing.
- Always listen to the whole thing. Mispronounced names are the most common
  embarrassment, and the most damaging when the name is a client's.

## Lesson 5.2 — Short video, cheaply

The pipeline that works on a phone:

**Script → voice or on-camera → b-roll → captions → music → export.**

CapCut does the middle three well. Auto-captions are now accurate enough for
English and increasingly for local languages; always proofread them, because a
caption error is a permanent, public error.

## Lesson 5.3 — The repurposing engine

One recording becomes many assets. This is the highest-return media workflow in
small organisations.

| Source | Becomes |
|---|---|
| 20-minute training | 5 short clips, 1 written guide, 10 quote graphics |
| 3-minute interview | 3 vertical clips, 1 article, 6 captions |
| A sermon or talk | 4 clips, 1 summary, 1 study guide |

## Lesson 5.4 — The honesty rules

::: warn
**Three rules that keep you out of trouble.**

1. Do not generate a voice that sounds like a specific real person without their
   written consent.
2. Do not present generated footage as real event footage.
3. Disclose synthetic media where a viewer would reasonably feel deceived.
:::

::: exercise
**Exercise 5.4 — Produce one repurposed set**

1. Record three minutes on a topic you know.
2. Transcribe it with AI.
3. Cut three vertical clips with captions.
4. Generate a written summary from the transcript.
5. Publish all four. Note which performed best.

**Time:** 60 minutes. **Deliverable:** four published assets from one recording.
:::

# Module 6 — Agents: When AI Takes Actions

## Lesson 6.1 — What an agent is

An assistant answers. An agent acts. It can look something up, write it
somewhere, send it to someone, and decide what to do next based on what it finds.

The moment a system can act, the failure modes change from "wrong answer" to
"wrong action taken". That is a different category of risk.

## Lesson 6.2 — The permission ladder

Build in this order, and do not skip a rung.

| Level | The agent may | Risk |
|---|---|---|
| **1. Read** | Look things up and report | Low |
| **2. Draft** | Prepare an action for human approval | Low |
| **3. Act with confirmation** | Perform the action after a human clicks approve | Medium |
| **4. Act within limits** | Perform small actions unsupervised, log everything | High |
| **5. Act freely** | — | Do not do this |

Most small organisations should live permanently at level 2 or 3. The value is in
removing preparation work, not in removing the human.

## Lesson 6.3 — Designing the guardrails

Every agent needs four limits, written down:

1. **Scope** — exactly which systems and records it may touch.
2. **Spend cap** — the maximum money it can commit without approval. Often zero.
3. **Escalation** — the conditions under which it stops and asks.
4. **Log** — every action recorded, with a timestamp, reviewable.

::: warn
**Never give an agent unrestricted access to money, email sending, or deletion.**
A hallucination that costs you a customer is bad. A hallucination that sends 400
emails or deletes a folder is a catastrophe.
:::

::: exercise
**Exercise 6.3 — Design a level-2 agent**

1. Choose a repetitive process: enquiry triage, invoice preparation, report
   assembly.
2. Write its scope, spend cap, escalation rule and log.
3. Build the simplest version that drafts rather than acts.
4. Run it for one week with a human approving every output.
5. Count how many drafts the human accepted unchanged.

**Time:** 90 minutes. **Deliverable:** a working level-2 agent and an acceptance
rate.
:::

# Module 7 — Testing and Evaluation

## Lesson 7.1 — The evaluation set

Before you ship, write down what "working" means, in numbers.

- Twenty test questions with correct answers.
- A pass threshold (for example, eighteen of twenty).
- A tone rubric, scored by a human.
- A safety list: ten things it must never say or do.

Run the evaluation after every change. This is the difference between a tool and
a toy.

## Lesson 7.2 — Red teaming

Try to break your own system, deliberately, before a customer does.

The standard attack list: false premises, out-of-scope requests, attempts to
extract the instructions, requests in another language, deliberately ambiguous
questions, and emotional manipulation.

Record every success as a bug. Fix it with a rule, then add that attack to the
permanent test set.

## Lesson 7.3 — Monitoring after launch

A tool that is not monitored decays. Documents go out of date, prices change, and
the tool keeps confidently quoting the old ones.

Set a monthly review: read twenty real conversations, check for outdated answers,
update the source pack, re-run the evaluation.

::: exercise
**Exercise 7.3 — Red team your own build**

1. Write your ten-item safety list.
2. Attack your system with all ten.
3. Fix every success.
4. Add all ten attacks to the permanent test set.
5. Schedule the monthly review now.

**Time:** 45 minutes. **Deliverable:** a documented test set and a review date.
:::

# Module 8 — Capstone: Ship a Tool

## Lesson 8.1 — The brief

Ship one tool that other people use without you: a grounded assistant, an image
system, a media pipeline, or a level-2 agent. It must have an evaluation set, a
named owner, a monitoring plan, and documentation a non-technical colleague can
follow.

## Lesson 8.2 — The rubric

| Criterion | Weight | Excellent | Weak |
|---|---|---|---|
| Grounding | 25% | Answers only from sources; refuses correctly | Invents answers |
| Evaluation | 25% | Documented test set, score before and after | "I tried it and it seemed fine" |
| Safety | 20% | Red-teamed, guardrails documented | No limits |
| Ownership | 15% | Named owner, monthly review scheduled | Nobody responsible |
| Documentation | 15% | A colleague can operate and maintain it | Only the builder understands it |

::: scripture
"Let all things be done decently and in order."
— 1 Corinthians 14:40
:::

Order is not bureaucracy. Order is what lets a good thing keep working after the
person who built it has moved on to the next thing.

::: exercise
**Exercise 8.2 — Ship it**

1. Build the tool.
2. Run the evaluation and record the score.
3. Red team it.
4. Hand it to a colleague and watch them use it without your help.
5. Present in five minutes: what it does, what it scores, what it cannot do, who
   owns it.

**Time:** 90 minutes. **Deliverable:** a shipped tool with documentation.
:::

# Module 9 — The Next Tier

**AI-401 Specialist** is for the people who will govern and sell this work:
writing policy that survives an audit, evaluating tools on evidence, managing
data-protection obligations, training staff at scale, and scoping and pricing
consulting engagements.

Take it when you have shipped at least one tool and maintained it for a month.
The Specialist tier assumes you know what breaks in production, because that
knowledge is what makes governance credible rather than theoretical.
