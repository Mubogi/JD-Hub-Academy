# Module 1 — The Specialist's Job

Every organisation in this region is being told to "adopt AI" by donors,
head offices, boards and consultants. Almost none of them have anyone who can
tell the difference between a real capability and a demonstration. That gap is
the specialist's job, and it is well paid because the cost of getting it wrong is
measured in money and reputation.

A specialist does four things:

1. **Govern** — write the rules, and make them stick.
2. **Evaluate** — decide what to buy and what to reject, on evidence.
3. **Train** — bring staff to competence at three levels.
4. **Deliver** — scope, price and complete engagements.

::: scripture
"If the ax is dull and its edge unsharpened, more strength is needed, but skill
will bring success."
— Ecclesiastes 10:10
:::

Skill brings success. Effort without skill is expensive; this tier is about the
edge, not the swinging.

## Lesson 1.1 — The three questions every client asks

Learn these and you will never be lost in a first meeting.

**"Will this replace my staff?"** The honest answer: it changes which tasks
matter. The people who will struggle are those whose entire role is one
repetitive task and who refuse to learn the adjacent judgement work. Answer with
specifics about their roles, not general reassurance.

**"Is it safe?"** The honest answer: it is as safe as your policy, your training
and your data handling. That is what they are actually buying from you.

**"How much will it save?"** The honest answer: it depends on the task, and here
is how we will measure it before we promise anything.

## Lesson 1.2 — What separates a specialist from an enthusiast

| Enthusiast | Specialist |
|---|---|
| Shows what the tool can do | Shows what it fails at |
| Recommends a tool | Recommends a process, with a tool inside it |
| Measures activity | Measures outcome, with a method |
| Promises savings | Estimates, then verifies |
| Hides the risks | Documents the risks and the owner of each |
| One big rollout | One bounded pilot, then scale |

::: exercise
**Exercise 1.2 — Write your position**

1. Write, in 150 words, what you will and will not claim about AI.
2. Include one thing you know it cannot do well.
3. Read it aloud. If it sounds like a sales pitch, rewrite it.

**Time:** 20 minutes. **Deliverable:** your professional position statement.
You will use it in every proposal.
:::

# Module 2 — AI Governance and Policy

## Lesson 2.1 — What a policy must do

A policy has four jobs, and most organisational policies fail at three of them.

1. **Tell people what is allowed.** Specific, not aspirational.
2. **Tell people what is forbidden.** Especially data.
3. **Say who is accountable.** A named role, not "the organisation".
4. **Say how it is enforced and reviewed.** Or it is decoration.

## Lesson 2.2 — The structure that survives audit

| Section | Content |
|---|---|
| **Purpose & scope** | Who and what it covers; which tools |
| **Permitted use** | Approved tools; approved data; approved purposes |
| **Prohibited data** | The never-list, in plain language |
| **Human review** | Which outputs require a named reviewer before release |
| **Disclosure** | When AI assistance must be stated externally |
| **Accountability** | Named owner per use case; escalation route |
| **Training** | Who must be trained, on what, how often |
| **Review** | Date, reviewer, and what triggers an off-cycle review |

## Lesson 2.3 — The data classification that does the work

The single most useful governance artefact is a three-tier data classification.
Everything else follows from it.

| Tier | Examples | May go into a public AI tool? |
|---|---|---|
| **Public** | Published prices, marketing copy | Yes |
| **Internal** | Internal reports, draft strategy, staff lists | Only in an approved enterprise tool with training disabled |
| **Restricted** | Client identity data, health, financial records, credentials, contracts | Never in a public tool. Only in an approved private deployment |

Publish this as a one-page table. Train against it with real examples from the
organisation. It prevents more incidents than any long document.

## Lesson 2.4 — The roll-out that does not fail

1. **Baseline.** What is already being used, informally, by whom. (There is
   always shadow usage. Finding it is the first job.)
2. **Pilot.** One department, one workflow, eight weeks, measured.
3. **Publish.** Policy plus classification plus approved tools, in one page each.
4. **Train.** All staff at level one; the pilot team at level two.
5. **Review.** Quarterly, with the incident log as the agenda.

::: warn
**Banning is not governance.** An outright ban drives usage underground and
removes your visibility. The aim is visibility and safe use, not prohibition.
:::

::: exercise
**Exercise 2.4 — Write a real policy**

1. Take a real organisation you know.
2. Write the seven sections, in under three pages.
3. Build the three-tier data table with five real examples per tier.
4. Test it: give it to a staff member and ask what they would do with a specific
   document.

**Time:** 75 minutes. **Deliverable:** a policy that a staff member can follow
without asking you.
:::

# Module 3 — Evaluation and Procurement

## Lesson 3.1 — The evaluation grid

Never compare tools by demonstration. Compare them on your own tasks, scored.

| Criterion | Weight | How you score it |
|---|---|---|
| Accuracy on your test set | 30% | 20 real tasks, scored blind |
| Data handling | 20% | Where data is stored, retention, training use |
| Integration | 15% | Does it fit the systems you already run |
| Total cost | 15% | Licence plus training plus support, three years |
| Support & local availability | 10% | Can you get help in your timezone |
| Exit | 10% | How hard is it to leave, and to take your data |

That last row is the one nobody asks about and everybody regrets. A tool you
cannot leave is a hostage situation with a subscription.

## Lesson 3.2 — Running a blind test

The method that survives scrutiny:

1. Write twenty real tasks with correct answers.
2. Have two people score outputs without knowing which tool produced them.
3. Record disagreements. They usually reveal a criterion you forgot to define.
4. Report scores with the method attached.

## Lesson 3.3 — The three-year cost

Licence fees are the smallest number. The real cost includes training time,
process redesign, integration, support, and the cost of switching later. A tool
that costs twice as much but requires no training can be cheaper.

::: exercise
**Exercise 3.3 — Score two real tools**

1. Pick two tools that claim to do the same job.
2. Write ten real tasks with correct answers.
3. Run both, score blind.
4. Fill the evaluation grid including three-year cost and exit.
5. Write the recommendation in five sentences.

**Time:** 90 minutes. **Deliverable:** a procurement recommendation a committee
could sign.
:::

# Module 4 — Data Protection and Risk

## Lesson 4.1 — The questions to ask any vendor

- Where is our data stored, physically?
- Is it used to train models? Can we switch that off in writing?
- How long is it retained, and can we delete it on demand?
- Who inside your company can read it?
- What happens to our data if we stop paying?
- Which sub-processors do you use?

Get the answers in writing. A verbal assurance is not a control.

## Lesson 4.2 — The risk register

Five risks every AI deployment carries. Document them, with an owner and a
mitigation.

| Risk | Mitigation | Owner |
|---|---|---|
| Sensitive data entered into a public tool | Classification + training + approved tools | Data protection lead |
| Wrong output published | Named reviewer before release | Line manager |
| Over-reliance, skill decay | Periodic manual audits of AI-assisted work | Department head |
| Vendor lock-in | Exit clause, data export tested annually | Procurement |
| Regulatory change | Quarterly policy review | Compliance |

## Lesson 4.3 — What the law expects

Data-protection law in most jurisdictions — including Uganda's Data Protection
and Privacy Act — rests on the same principles: lawful basis, purpose
limitation, minimisation, accuracy, storage limitation, security, and the rights
of the data subject.

AI does not create new principles; it makes old ones harder to satisfy. A
customer's data sent to a model in another country is still their data. Personal
data in a prompt is still processing.

::: warn
**This course is not legal advice.** Regulations differ and change. For any
deployment involving personal data at scale, get a local opinion in writing.
What you can do is arrive at that meeting with the right questions — which is
most of the value.
:::

::: exercise
**Exercise 4.3 — Build a risk register**

1. Choose a real AI deployment, existing or planned.
2. Fill all five risks with mitigations and named owners.
3. Add any risk specific to that organisation.
4. Test one mitigation: is it actually in place, or only on paper?

**Time:** 45 minutes. **Deliverable:** a risk register with one verified control.
:::

# Module 5 — Training Design at Scale

## Lesson 5.1 — Three curricula, not one

| Level | Audience | Content | Duration |
|---|---|---|---|
| **Awareness** | All staff | What it is, the data rule, the disclosure rule | 90 minutes |
| **Practitioner** | Staff who produce documents | R-T-C-F, verification, their three main tasks | 2 days |
| **Builder** | One or two per department | Grounded assistants, evaluation, ownership | 5 days |

Most organisations buy one training for everyone and wonder why nothing changes.
The awareness session changes behaviour; the practitioner session changes output;
the builder session creates internal capability. You need all three, in that
order.

## Lesson 5.2 — The training that transfers

What makes training stick, in order of importance:

1. **Their own work.** Every exercise uses the learner's real task.
2. **A named follow-up.** One task, one week later, checked by a manager.
3. **A peer who can help.** At least two people per department trained, so
   nobody is alone.
4. **A library they contributed to.** Prompts they wrote themselves.
5. **Visible leadership use.** If managers do not use it, staff conclude it is
   optional.

## Lesson 5.3 — Measuring training

Do not measure satisfaction. Measure behaviour.

- Before and after: how many staff can complete a specified task with AI in
  under X minutes, to an acceptable standard?
- Thirty days later: how many are still doing it?
- Ninety days later: what changed in output volume or response time?

::: exercise
**Exercise 5.3 — Design a curriculum**

1. Choose an organisation and a department.
2. Write the awareness session outline (90 minutes).
3. Write the practitioner outline (two days), with six exercises on their own
   work.
4. Define the three measurement points.
5. Write the one-sentence follow-up task each learner must complete in week one.

**Time:** 60 minutes. **Deliverable:** a curriculum with measurable outcomes.
:::

# Module 6 — Consulting: Scoping, Pricing, Delivering

## Lesson 6.1 — The scoping conversation

Never quote before you understand four things:

1. **The task** — what specifically takes too long or goes wrong.
2. **The volume** — how often, how many people.
3. **The constraint** — data sensitivity, systems, budget, politics.
4. **The decision-maker** — who signs, and what they need to see.

If you cannot state the task in one sentence, you are not ready to quote.

## Lesson 6.2 — Pricing models

| Model | When to use | Risk |
|---|---|---|
| **Fixed fee** | Clear scope, known deliverable | You absorb the surprises |
| **Day rate** | Exploratory or advisory | Client caps the days |
| **Retainer** | Ongoing support and review | Scope creep if undefined |
| **Value-based** | You can measure the saving | Requires baseline data and trust |
| **Training per cohort** | Standard curriculum | Logistics and venue |

For a first engagement with a new client, fixed fee with a written scope is
usually best. It builds trust and protects you from unlimited discovery.

## Lesson 6.3 — The proposal that wins

One page. Five sections.

::: box
**1. The problem, in their words.** Quote their own description back to them.

**2. What we will do.** Three to five deliverables, each with a date.

**3. What it will achieve.** The metric, the baseline, the target.

**4. What it costs.** The number, what is included, what is not.

**5. What we need from you.** Named people, access, decisions, by when.

Signed acceptance: ______________________
:::

Section five is the one that separates professionals from hopefuls. An engagement
where the client owes you nothing is an engagement that will drift.

## Lesson 6.4 — Delivery discipline

- **Week one:** baseline measurement. Non-negotiable. Without it you cannot
  prove value later.
- **Weekly:** one short written update. Three lines. Decisions needed, progress,
  risks.
- **Midpoint:** show something working, even if partial. Momentum depends on it.
- **Close:** the measured result, the documentation, the handover, and one named
  person trained to maintain it.

::: scripture
"A good name is to be chosen rather than great riches, loving favour rather than
silver and gold."
— Proverbs 22:1
:::

In consulting, your name is your entire asset. One engagement where you promised
a saving you did not verify will follow you for years. One engagement where you
reported honestly that the saving was smaller than hoped, and explained why, will
bring you referrals — because it is rare.

::: exercise
**Exercise 6.4 — Write a real proposal**

1. Pick a real organisation you could genuinely help.
2. Write the one-page proposal, all five sections.
3. Include a baseline measurement in week one.
4. Price it three ways (fixed, day rate, value-based) and decide.
5. Send it. Actually send it.

**Time:** 60 minutes. **Deliverable:** a sent proposal.
:::

# Module 7 — Building Your Practice

## Lesson 7.1 — The service ladder

Sell in this order. Each rung funds the next and proves capability for it.

1. **Awareness training** — low price, high volume, builds reputation.
2. **Workflow audit** — a fixed-fee diagnostic that produces a report.
3. **Implementation** — build the workflow or tool.
4. **Retainer** — monthly review, updates, new use cases.
5. **Governance** — policy, evaluation, procurement support.

Most people try to sell rung three first, having never done rung one, to an
organisation that does not yet trust them. That is why it takes so long.

## Lesson 7.2 — What to publish

You do not need a marketing budget. You need evidence.

- One case study per engagement, with the measured number and the client's
  permission.
- One short piece per month on a problem your clients actually have.
- Your policy template, freely available. It creates trust and inbound enquiries.

## Lesson 7.3 — The ethics that protect you

::: warn
**Four things never to do.**

1. Promise a saving you have not measured.
2. Deploy something you have not red-teamed.
3. Take a client's data into a tool you have not vetted.
4. Sell a tool you would not use yourself.
:::

::: exercise
**Exercise 7.3 — Build the ladder**

1. Write your five-rung service ladder with a price for each.
2. Write one case study from work you have already done.
3. Publish one piece of writing this month.
4. Identify three organisations for rung one.

**Time:** 60 minutes. **Deliverable:** a priced ladder and one published piece.
:::

# Module 8 — Capstone: The Advisory Pack

## Lesson 8.1 — The brief

Produce a complete advisory pack for a real organisation: a policy, a data
classification, a risk register, a training plan, a tool evaluation, and a
one-page proposal for the first engagement.

## Lesson 8.2 — The rubric

| Criterion | Weight | Excellent | Weak |
|---|---|---|---|
| Policy usability | 20% | A staff member follows it unaided | Reads well, unusable |
| Evaluation rigour | 20% | Blind scoring, documented method | Demo-based opinion |
| Risk honesty | 20% | Real risks, named owners, verified controls | Generic list |
| Training design | 20% | Three levels, measurable, own-work exercises | One-size session |
| Commercial clarity | 20% | One page, priced, with a baseline commitment | Vague scope |

::: scripture
"Commit your works to the Lord, and your thoughts will be established."
— Proverbs 16:3
:::

::: prayer
**A closing reflection**

Lord, give me the discipline to measure before I promise, the honesty to report
what I find, and the humility to say "I do not know" when it is true. Let the
work I do make other people's work lighter and their judgement sounder.
Amen.
:::
