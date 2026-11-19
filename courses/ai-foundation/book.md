# Module 1 — What Artificial Intelligence Actually Is

Most people are told to "learn AI" and handed a login screen. That is like being
told to learn to drive by being handed a set of keys. This module gives you the
map before the keys: what the machine is doing, why it fails, and what it means
for your work.

Read this module even if you are impatient. Almost every mistake people make
with AI — in business, in school, in church administration, in public
communication — comes from misunderstanding one of the three ideas here.

## Lesson 1.1 — It predicts. It does not know.

A large language model has one job. Given the text so far, it guesses what text
should come next. That is the entire mechanism. There is no database of facts
inside it, no search, no understanding in the human sense. It is an
extraordinarily good pattern-guesser trained on an enormous quantity of writing.

This matters because the output *looks* like knowledge. It arrives in complete
sentences, with confidence, in good grammar. Your brain reads fluency as
competence. It is not. Fluency is a property of the writing; competence would be
a property of the understanding, and there is none.

::: scripture
"The simple believes every word, but the prudent considers well his steps."
— Proverbs 14:15
:::

That single verse is a complete AI policy. The tool is not the danger.
Unconsidered belief is the danger. A prudent person uses the tool *and*
considers their steps.

**What this means practically.** When the AI gives you an answer, you are not
receiving information. You are receiving a well-formed guess. For low-stakes
tasks — brainstorming, rephrasing, drafting — a good guess is exactly what you
want and it saves you real time. For high-stakes tasks — a legal clause, a
medical dose, a tax figure, a quotation to a client — a good guess is a
liability until you have checked it.

## Lesson 1.2 — The three failure modes

Every AI problem you will ever encounter is one of these three. Learn the names
and you will diagnose faster than most consultants.

| Failure | What it looks like | Your defence |
|---|---|---|
| **Hallucination** | A specific, confident, invented fact. A citation that does not exist. A law that was never passed. | Verify anything that carries a consequence |
| **Bias** | Output that reflects the skew in the training data — who was written about, and who was not | Ask "who is missing from this answer?" |
| **Leakage** | Your private data leaves your control and may be stored, reviewed, or used for training | Never paste secrets. Know the settings |

### Hallucination in detail

Hallucination is not the AI lying. Lying requires knowing the truth and choosing
against it. The model has no truth to compare against. It generates the most
probable continuation, and sometimes the most probable continuation of
"According to the 2019 study by..." is a plausible-sounding author name that has
never existed.

It gets worse in a specific way: hallucination is *most* likely exactly where
you most need accuracy — niche topics, local facts, recent events, numbers, and
citations. The model has less training signal there, so it fills the gap with
plausible invention.

::: warn
**The citation trap.** AI tools will produce references that look perfect:
author, year, journal, volume, page numbers, DOI. A meaningful share of them do
not exist. Never cite a source you have not opened yourself. This is the
fastest way to destroy your credibility in an academic or professional setting.
:::

### Bias in detail

The model learned from text produced by humans, and humans are uneven. If the
training material discussed business leadership mostly through the example of
men in Europe and North America, then "a typical business leader" in the model's
patterns looks like that. Ask it to describe a doctor, a farmer, a criminal, a
beautiful person, or a competent manager, and you will see the pattern surface.

This is not a reason to abandon the tool. It is a reason to *ask better
questions* — "give me five very different examples, including ones from East
Africa and from rural settings" — and to review output for who got left out.

### Leakage in detail

Anything you type into a consumer AI tool may be stored, may be reviewed by
humans for quality, and in some products may be used to improve the model. Once
sent, you cannot recall it.

Never enter: national ID numbers, bank or mobile-money details, passwords,
client medical records, salary data, unreleased contracts, or another person's
personal data without their consent. If you would not read it aloud in a
marketplace, do not type it into a chatbot.

## Lesson 1.3 — What AI is not

Clearing up four confusions saves months of wasted effort.

**It is not a search engine.** A search engine retrieves pages that exist and
shows you where they are. A language model generates text that sounds like an
answer. When you need a *source*, use search or a research tool with citations.
When you need a *draft*, use the model.

**It is not a database.** It cannot reliably recall your stock levels, your
client list, or last month's figures. It can help you *work with* that data if
you give it the data.

**It is not a professional.** It will discuss your medical symptoms, your tax
position, and your contract dispute with total confidence and no accountability.
It has never met you, cannot examine you, and cannot be sued. Use it to prepare
questions for the professional, not to replace them.

**It is not conscious.** It does not want anything, know anything, or care about
you. When it says "I understand how you feel," that is a sequence of tokens that
statistically follows the preceding ones.

::: box
**The intern metaphor — keep this for the whole course**

Imagine a brilliant, fast, tireless intern who has read everything, works at
3 a.m., never complains — and is completely confident even when wrong, has no
loyalty to you, and will not tell you when they are out of their depth.

You would use that intern constantly. You would also read their work before it
reached a client. That is the entire discipline of working with AI, and it fits
in one sentence.
:::

## Lesson 1.4 — Where AI genuinely earns its keep

Know what you are buying before you spend time learning it. AI is strongest at
four things.

**1. Transforming text you already have.** Make it shorter, longer, warmer,
more formal, simpler, translated, structured into a table, turned into action
points. This is where AI is almost always correct and almost always fast,
because it is not inventing facts — it is reshaping yours.

**2. Producing first drafts.** The blank page is the enemy of productivity. AI
removes the blank page. You then do the part that requires judgement: deciding
what is good.

**3. Generating options.** Ten headline variants, five ways to explain a
concept, three objections a customer might raise. Divergent thinking at speed.

**4. Working across formats.** A document becomes a summary, a summary becomes
slides, slides become a script, a script becomes captions. This is the biggest
time saving in most small businesses, and almost nobody uses it.

It is weakest at: verified facts, arithmetic you have not checked, recent local
information, anything requiring accountability, and anything requiring taste
that has not been described to it.

::: scripture
"See then that you walk circumspectly, not as fools but as wise, redeeming the
time, because the days are evil."
— Ephesians 5:15–16
:::

Redeeming the time is the honest case for this technology in a small business.
Not novelty. Not hype. Hours returned to you — for customers, for family, for
the work only you can do.

::: exercise
**Exercise 1.4 — Meet the machine**

Do this on your own phone, with your own work.

1. Open any AI assistant (ChatGPT, Gemini, or Meta AI inside WhatsApp).
2. Ask it: *"What do you know about my business?"* using your actual business
   name and town. Read the answer carefully.
3. Ask it: *"What are three things you just told me that you might have
   invented?"* This is a genuinely useful question and the answer is often
   illuminating.
4. Write down, in one sentence, whether you would send that answer to a customer.

**Time:** 15 minutes. **Deliverable:** one sentence in your notebook.
:::

# Module 2 — Prompting: Getting Usable Answers

Prompting is not a magic phrase. It is the skill of giving clear instructions,
which is the same skill that makes you good at briefing a member of staff. If
you can brief a person, you can brief a model — you just have to be more
explicit, because the model cannot see the situation, cannot ask you a
clarifying question unless you invite one, and will not tell you it is confused.

## Lesson 2.1 — The R-T-C-F structure

Four elements. Every strong prompt has most of them; the weak prompts you have
seen are missing two or three.

| Element | Question it answers | Example |
|---|---|---|
| **R — Role** | Who should the AI be? | "You are a copywriter for small food businesses" |
| **T — Task** | What exactly must it do? One verb. | "Write three Instagram captions" |
| **C — Context** | What does it need to know? | "A bakery in Kumasi launching delivery. Friendly tone." |
| **F — Format** | What should the output look like? | "Max 40 words each, end with a question" |

Compare:

::: box
**Weak:** "Write about my business."

**Strong:** "You are a copywriter for small food businesses. Write three
Instagram captions for a bakery in Kumasi launching delivery. Friendly tone,
speak to busy parents. Max 40 words each, end with a question."
:::

The weak version is not wrong. It is *underspecified*, so the model guesses, and
its guesses are generic because generic text is the most statistically likely
text. The strong version constrains the guess into the region you actually want.

### Why each element does work

**Role** narrows the vocabulary and the assumptions. "You are an accountant"
changes the register, the cautions, and the structure of the answer.

**Task** with a single clear verb prevents the model from doing three things
badly instead of one thing well.

**Context** is where most of the value lives. Audience, tone, length, facts,
constraints, what to avoid. Every detail you add removes a guess.

**Format** is the most under-used element and the fastest win. "Give me a table
with three columns", "five bullets, no more than twelve words each", "an email
with a subject line" — the output becomes immediately usable instead of
something you have to reformat.

## Lesson 2.2 — Iteration: the first answer is a draft

Beginners judge the first answer. Professionals treat it as material.

The four follow-up moves that cover most situations:

1. **Adjust the shape.** "Make it shorter." "More formal." "Warmer." "Simpler —
   explain it to someone who did not finish secondary school."
2. **Ask for options.** "Give me five versions and I will choose." Never accept
   the first idea when you can have five in the same amount of time.
3. **Interrogate it.** "What did you assume that I did not tell you?" This
   surfaces the guesses and lets you correct them. It is the single most useful
   question in this course.
4. **Ask it to critique itself.** "Which of these three is weakest, and why?"
   Then ask it to fix that one.

::: note
**The two-turn rule.** Almost every disappointing AI result is one turn away from
being good. When something is nearly right, do not start over — say what is
wrong. "The tone is too formal and the third paragraph repeats the first." That
sentence costs eight seconds and fixes the output.
:::

## Lesson 2.3 — Giving it something to work with

The highest-quality AI output almost always comes from giving the model
*material*, not just instructions.

- Paste the actual customer email you need to reply to.
- Paste your rough notes and ask for them organised.
- Upload the price list and ask for a quotation.
- Paste your competitor's page and ask what they are claiming.
- Paste your own previous good work and say "match this voice."

This is the difference between asking a colleague "write me something about
pricing" and handing them your price list, your last three customer emails, and
your brand guidelines. Same colleague, wildly different output.

::: exercise
**Exercise 2.3 — The three-round improvement**

Choose one real task from your work this week.

1. **Round 1.** Write a prompt the way you naturally would. Save the output.
2. **Round 2.** Rewrite the prompt using R-T-C-F. Save the output.
3. **Round 3.** Take the Round 2 output and apply two follow-up moves from
   Lesson 2.2. Save the output.

Keep all three. At the end of the course you will look back at Round 1 and be
embarrassed, which is the correct response and a reliable sign of progress.

**Time:** 25 minutes. **Deliverable:** three screenshots or saved documents,
labelled Round 1, 2, 3.
:::

## Lesson 2.4 — Voice: talking to the machine

Typing is not the only way in. Every major assistant now accepts voice, and for
many people — especially those who think faster than they type, or who find
typing in English laborious — speaking is dramatically better.

Speak the way you would brief a competent assistant: situation, task, audience,
tone, length. The transcription is good enough that you can speak naturally. You
can also speak in Luganda or Swahili and ask for the answer in English, or the
reverse, which is one of the most practically useful features for East African
users and one almost nobody teaches.

::: exercise
**Exercise 2.4 — Speak a prompt**

1. Open the voice input on ChatGPT, Gemini or Meta AI.
2. Speak a full brief for a real task — at least thirty seconds of speech.
3. Read the transcript. Notice what you said that you would never have typed,
   and whether the answer was better for it.
4. Then try: speak in your first language, ask for the output in English.

**Time:** 15 minutes. **Deliverable:** the transcript, and one sentence on
whether voice beat typing for you.
:::

# Module 3 — ChatGPT: The General Workhorse

ChatGPT is the most widely used general assistant, and for good reason: it is
competent across writing, analysis, files, images and voice, and the free tier is
genuinely usable. This module gets you past "chatting" and into working.

## Lesson 3.1 — What it is good at, and what to hand elsewhere

**Strong:** drafting and rewriting, summarising, structuring messy notes,
explaining concepts at a chosen level, brainstorming, working with an uploaded
document or spreadsheet, translation, tone adjustment.

**Weaker:** current local facts (use a search-grounded tool), precise arithmetic
over many rows (use a spreadsheet), verified citations (verify yourself), and
anything where being wrong is expensive.

## Lesson 3.2 — The five work patterns

Almost all real business use of ChatGPT falls into five patterns. Learn the
pattern, not the button.

**Pattern 1 — The rewrite.** Give it text, say what to change. *"Rewrite this
paragraph to be half the length and less apologetic, keeping every fact."*

**Pattern 2 — The brief.** Give it the situation, get a draft. *"You are a
bookkeeper. Write a 90-word second reminder for a 14-day overdue invoice, firm
but friendly, to a long-standing client."*

**Pattern 3 — The summarise-and-extract.** Give it a long document, ask for
specific things. *"From this contract, list the payment terms, the termination
notice period, and anything that limits my liability."*

**Pattern 4 — The options generator.** Ask for variety, then choose.
*"Give me eight names for a mobile phone repair shop, none ending in 'Hub' or
'Tech', and explain the strongest one."*

**Pattern 5 — The tutor.** Ask it to teach you. *"Explain VAT registration in
Uganda to me as if I am a shop owner with no accounting background, then give me
three questions to ask my accountant."*

## Lesson 3.3 — Working with files

You can upload documents, spreadsheets and images and ask questions about them.
This is the feature that changes work most, and the one most people never try.

Useful prompts for an uploaded document:

```prompt
Summarise this document in five bullets for someone who has 60 seconds.
Then list every figure that appears, with the sentence it came from.
Then tell me what the document does NOT cover that I should ask about.
```

That third instruction is the one that makes you look sharp in a meeting.

::: warn
**Before you upload anything**, check it does not contain client identity
numbers, bank details, medical records, or third-party personal data. If it does,
remove those pages first, or use a tool your organisation has approved for
confidential material.
:::

## Lesson 3.4 — Custom instructions: stop repeating yourself

Every serious assistant lets you set persistent context: who you are, what you
do, how you want answers. Set it once and every future conversation starts
already briefed.

Write it in four lines:

1. Who you are and what your work is.
2. Who your audience is.
3. How you want answers: length, tone, format.
4. What you never want: invented facts, excessive apology, emoji, jargon.

This single setting is worth more than any prompt trick. It removes the
"explain my business again" tax from every conversation.

::: exercise
**Exercise 3.4 — Build your standing brief**

1. Write your four-line standing brief in a notes app.
2. Paste it into the custom instructions of your main assistant.
3. Start a fresh conversation and ask a normal work question.
4. Compare the answer to what you would have got before.

**Time:** 20 minutes. **Deliverable:** your four lines, saved. You will reuse
this for the rest of the course and after it.
:::

# Module 4 — Google Gemini in Daily Work

Gemini's advantage is not that it is smarter. It is that it is *already where
your work is* — inside Gmail, Docs, Sheets and Drive, and on Android phones. The
friction of opening a separate app is what kills most AI habits. Gemini removes
that friction.

## Lesson 4.1 — The assistant inside your inbox

The highest-value use in this module is email. A long thread is a tax on your
attention. Gemini summarises it and drafts the reply.

```prompt
Summarise this email thread: the decisions made, the open questions,
and who owes what by when.
```

```prompt
Draft a reply that agrees to the first two points, politely declines the
third with a reason, and proposes a meeting next week. Keep it under
120 words.
```

Then the question that separates good from careless: *"What did you leave out of
that summary that might matter?"*

## Lesson 4.2 — Docs and Sheets

In Docs, give it your rough outline and ask for structure. In Sheets, describe a
calculation in plain English and ask for the formula — then ask it to explain
the formula, which is how you actually learn.

```prompt
Column D should be quantity in column C multiplied by the price in column B.
Write the formula for row 2, and explain in one sentence what each part does.
```

This is the fastest spreadsheet tutor ever built, and it is free.

## Lesson 4.3 — Research with sources

Gemini can ground answers in web results and show sources. That changes the
economics of research, but only if you actually open the sources. A link beside
a claim is not proof of the claim; it is an invitation to check.

The verification ritual — use it every time:

1. Does the source exist?
2. Does it actually say what the answer claims?
3. Is it recent enough to still be true?
4. Is it independent, or is it the company selling the thing?
5. What would the opposite view say?

## Lesson 4.4 — Knowing what it can see

Gemini may have access to your Gmail, Drive and calendar depending on your
settings. That is powerful, and it is a privacy decision you should make
deliberately rather than by accident.

Open the settings with a facilitator or a colleague and review, line by line,
what you have permitted. Turn off anything you cannot justify. This is not
paranoia; it is the same care you take with who has a key to your shop.

::: exercise
**Exercise 4.4 — The email thread test**

1. Find a real email thread with at least eight messages.
2. Summarise it with Gemini using the prompt in Lesson 4.1.
3. Read the summary against the thread. Find one thing it got wrong or left out.
4. Ask the follow-up question and see whether it catches the gap.
5. Draft your reply with AI, then edit it yourself before sending.

**Time:** 25 minutes. **Deliverable:** the summary, the gap you found, and the
final sent reply (redact names).
:::

# Module 5 — Meta AI in WhatsApp, Instagram and Facebook

This is the module that reaches the most people, because it requires no new app.
Meta AI sits inside WhatsApp, Instagram, Messenger and Facebook — the places
where East African business actually happens.

## Lesson 5.1 — Why this matters more than it sounds

A trader in Kampala does not need a productivity suite. She needs to answer
forty customer messages, post something today, and reply to a complaint without
losing the customer. All three of those happen inside apps she already has.

Meta AI in WhatsApp can answer questions in the chat, summarise a long thread or
voice note, generate images from a description, help write captions, and
translate. For a business owner, that is a complete marketing and customer
service department in one icon.

## Lesson 5.2 — The reply bank

The highest-value artefact you will build in this course is a reply bank: your
ten most common customer questions, each with a polished answer, saved as
WhatsApp Business quick replies.

| Customer asks | Your rough answer | Polished version |
|---|---|---|
| Do you deliver? | | |
| What is the price of…? | | |
| Can I pay on delivery? | | |
| Do you have another colour? | | |
| How long does it take? | | |
| Can I return it? | | |
| Do you offer discounts? | | |
| Where are you located? | | |
| Can I speak to the owner? | | |
| Do you do bulk orders? | | |

The prompt that fills the right-hand column:

```prompt
You are a customer-service writer for [business]. Rewrite each answer below
to be friendly, under 30 words, and end with a helpful next step.
Keep my prices and facts exactly as written — do not invent anything.
```

That last sentence — *do not invent anything* — is not decoration. Without it,
the model will helpfully "improve" your prices.

::: story
A second-hand clothes seller in Nakawa spent roughly two hours a day typing the
same six answers. She built a reply bank in one afternoon, saved the answers as
quick replies, and cut that to about twenty minutes. The time did not go into
"growth". It went into answering the *new* customers faster, which is where her
actual sales were coming from.
:::

## Lesson 5.3 — Captions and images that do not look generated

Meta AI can produce images from a description. Most people's first attempts look
like everyone else's first attempts: glossy, generic, slightly wrong hands.

Three rules that fix this:

**Describe the scene, not the concept.** "A woman in a green kitenge holding a
basket of tomatoes at a roadside stall in the morning light" beats "fresh
produce marketing image".

**Specify the style you want.** "Photograph, natural light, shallow depth of
field" or "flat vector illustration, two colours, no gradients".

**Use it for elements, not finished work.** Generated images are excellent as
backgrounds, textures, patterns and illustrations. They are weaker as
photographs of *your actual product*, which you should photograph yourself.

::: warn
**Disclosure and honesty.** If a customer would reasonably believe an image is a
photograph of your actual product or premises, and it is not, you are
misleading them. Say what it is, or use a real photo. This is both an ethical
rule and, in most jurisdictions, a legal one.
:::

## Lesson 5.4 — Turning a messy group into decisions

Group chats are where information goes to die. A genuinely useful habit: when a
long thread has run its course, ask the assistant to extract the decisions, the
open questions, and the action points with owners.

```prompt
From the conversation above, list: (1) decisions actually made, (2) questions
still open, (3) tasks with an owner and a deadline. If an owner was never
named, write UNASSIGNED.
```

That last clause is the whole trick. It makes the gaps visible, and visible gaps
get fixed.

::: exercise
**Exercise 5.4 — Build your reply bank**

1. List the ten questions customers actually ask you. Use your real messages,
   not guesses.
2. Fill in your rough answers.
3. Run the prompt above to polish them.
4. Correct anything the AI got factually wrong. This step is not optional.
5. Save them as quick replies in WhatsApp Business.

**Time:** 45 minutes. **Deliverable:** ten saved quick replies, and a note of
anything the AI got wrong that you had to fix.
:::

# Module 6 — Canva: Design Without a Designer

Design is not decoration. A poster that looks careless tells a customer that the
business is careless. Canva makes competent design achievable for someone with
no training, which is exactly the point — and the AI features inside it have
removed most of the remaining friction.

## Lesson 6.1 — The four rules that do most of the work

You do not need a design education. You need four rules, applied without
exception.

**1. One clear focus.** One headline, one image, one action. If everything is
big, nothing is.

**2. Three colours maximum.** One dominant, one secondary, one accent. More than
three reads as noise. Canva's Brand Kit enforces this for you.

**3. Two fonts maximum.** One for headings, one for body. Never more.

**4. Align to something.** Pick one edge — left, centre — and commit. Misaligned
elements are the most common tell of amateur design.

## Lesson 6.2 — The 30-minute poster sprint

Set a timer. Four steps, seven minutes each.

1. **Choose a template** that matches the *purpose*, not the prettiest one you
   see. A funeral announcement and a product launch need different structures.
2. **Strip it.** Delete every element you did not ask for. Empty space is not
   wasted space; it is what makes the important thing important.
3. **Fill it.** Headline (six words maximum), subhead, date and time, location,
   one call to action. That is all a poster needs.
4. **Fix it.** Apply the four rules. Step back. Squint. If the headline is not
   readable from three metres, it is too small.

## Lesson 6.3 — Magic Studio: what each tool is for

| Tool | Use it for | Do not use it for |
|---|---|---|
| **Magic Write** | Drafting copy inside the design | Final customer-facing claims |
| **Magic Media** | Backgrounds, textures, illustrations | Photos of your actual product |
| **Background Remover** | Product photos shot on a phone | Anything with fine detail like hair |
| **Magic Eraser** | Removing a distracting object | Removing watermarks you do not own |
| **Magic Resize** | One design to every format | Print without checking resolution |
| **Brand Kit** | Consistency across everything | — it is the highest-value feature |

**Magic Resize is the one to learn first.** One poster becomes an Instagram post,
a story, a WhatsApp status and an A5 flyer in about forty seconds. That single
feature replaces an hour of manual work per campaign.

## Lesson 6.4 — Export without embarrassment

- **Social media:** PNG, standard quality. JPG for photos.
- **Print:** PDF Print, and check the bleed settings.
- **WhatsApp:** compress before sending or it will be recompressed badly.
- **Never** export a 1080px design for an A2 banner. It will be blurry, and the
  printer will not warn you.

::: exercise
**Exercise 6.4 — The real poster**

Design a poster for a real event — yours, your church's, your business's. Not a
practice brief.

1. Run the 30-minute sprint.
2. Apply Magic Resize to four formats.
3. Show it to two people who are not in this course.
4. Ask one question only: "What is this asking me to do?"

If they cannot answer immediately, the poster failed and you know exactly what
to fix.

**Time:** 45 minutes. **Deliverable:** four exported formats.
:::

# Module 7 — The Content Engine: One Hour, One Week

Posting consistently is the hardest discipline in small-business marketing. Not
because content is hard, but because it is endless. This module turns it into a
system that runs in one sitting per week.

## Lesson 7.1 — The engine, in five steps

**Theme → angles → captions → images → schedule.**

Pick one theme for the week. Generate seven angles from it. Write captions for
each. Create one image style you reuse. Schedule them. Done.

The reason this works is that deciding *what to say* is the expensive part.
Writing is cheap once you know what to say. AI helps enormously with the second
and not at all with the first — which is why you start with a theme you chose.

## Lesson 7.2 — The prompt chain

Run these in sequence. Do not skip step one; it is what keeps the output from
being generic.

```prompt
Step 1 — You are a content strategist for [business], which serves [audience]
with [offer]. Give me seven content angles for next week: two educational,
two trust-building, two promotional, one personal story. One line each.
```

```prompt
Step 2 — For angle [X], write three caption options. Maximum 40 words,
friendly, one emoji at most, ending with a question or a call to action.
Include five relevant hashtags.
```

```prompt
Step 3 — Describe three simple image concepts for this caption that I can
create in Canva in under five minutes each. Be specific about layout and
about the text on the image.
```

```prompt
Step 4 — Turn this week's content into: one WhatsApp status (15 words),
one newsletter intro (80 words), and three story prompts.
```

```prompt
Step 5 — Suggest the best day and time to post each piece for [audience] in
[location], and explain the reasoning in one line each.
```

## Lesson 7.3 — The repurposing multiplier

One three-minute video can become: five short clips, ten captions, one newsletter
section, three quote graphics, and a written article. This is not laziness; it is
how professional media operations have always worked. AI simply makes it
available to a business with one employee.

::: exercise
**Exercise 7.3 — Schedule a week**

1. Choose your theme.
2. Run the five-step chain.
3. Edit every caption yourself. Delete anything that does not sound like you.
4. Build the images in Canva using one reusable template.
5. Schedule all seven in Meta Business Suite or Canva Content Planner.

**Time:** 60 minutes. **Deliverable:** seven scheduled posts, and the date you
will do this again next week, written in your diary.
:::

# Module 8 — Numbers, Admin and Money

This module is where AI saves the most time and where carelessness costs the
most money. Both statements are true at once.

## Lesson 8.1 — From plain English to formula

The spreadsheet is the most under-used business tool in East Africa, and the
reason is almost always formulas. That barrier is now gone.

```prompt
In Google Sheets, column D should show the total for each row: quantity in
column C multiplied by unit price in column B. Write the formula for D2.
Then explain each part in one short sentence so I understand it.
```

Then, when it breaks — and it will — paste the error and ask what went wrong.
This is the fastest way to learn spreadsheets that has ever existed.

## Lesson 8.2 — Cleaning messy data

Real business data is messy: inconsistent dates, "Yes"/"yes"/"YES", duplicate
customers, trailing spaces. AI can propose a cleaning plan, but the cleaning
itself should happen in the spreadsheet where you can see it.

```prompt
Here are the first ten rows of my sales sheet. Identify every inconsistency
you can see and give me a step-by-step cleaning plan. Do not guess at values;
tell me what to check.
```

## Lesson 8.3 — Documents that carry money

Quotations, invoices, receipts and statements must be exactly right. AI drafts
the *structure*; you check every number.

::: warn
**AI does not do arithmetic you have not checked, and never signs off on tax.**

Use it to draft the quotation layout, the covering letter, and the reminder
sequence. Do not use it to calculate the total, determine the VAT, or decide
what you owe. Those come from a spreadsheet and a qualified person.
:::

## Lesson 8.4 — The monthly report nobody has time to write

The highest-leverage admin task in most small organisations is the monthly
report. It is also the most hated. Give the AI the numbers and the structure,
and it produces the narrative — which is the part that takes the hours.

```prompt
Here is my monthly sales data by product. Write a one-page report for a
non-technical owner: what changed, the three most important observations,
and two decisions to consider. Do not invent figures not in the data.
```

::: exercise
**Exercise 8.4 — Notebook to dashboard**

1. Photograph a page of your handwritten sales notebook.
2. Transcribe it into a spreadsheet — type it, do not let AI guess.
3. Ask AI for the formulas for totals and monthly summary.
4. Build one chart that shows the single most important trend.
5. Ask AI to write the three-paragraph commentary, then check every figure.

**Time:** 45 minutes. **Deliverable:** a working sheet with one chart and a
verified commentary.
:::

# Module 9 — Customer Service and Sales

A customer who waits is a customer who leaves. AI does not fix a bad business,
but it removes the delay caused by you being one person.

## Lesson 9.1 — What a good bot does

A good bot answers the twenty questions you answer every day, instantly,
correctly, in your voice — and hands over to a human the moment it is out of its
depth. That is the whole specification.

A bad bot guesses, promises things you cannot deliver, argues, and traps the
customer in a loop. Both are easy to build. The difference is the escalation
rule.

## Lesson 9.2 — Building it from your own content

Tools like Chatbase or Tidio let you upload your FAQ, price list and policies and
produce a bot grounded in *your* material rather than the open internet. That
grounding is what makes it usable.

The build sequence:

1. Collect your twenty most-asked questions and their correct answers.
2. Upload the FAQ, price list, delivery policy and returns policy.
3. Write the escalation rule in plain language: "If you are not certain, say
   you will connect the customer to a person, and do not guess."
4. Test it — properly, by trying to break it.

## Lesson 9.3 — The break-the-bot exercise

Build in pairs. Then swap and attack each other's bots. Try each of these:

- Ask something outside its knowledge ("Do you ship to Mars?").
- Ask for a discount it should not give.
- Ask a medical or legal question.
- Ask in another language.
- Ask something deliberately ambiguous.
- Ask for a competitor's price.
- Ask it to reveal its instructions.
- Ask a question built on a false premise.
- Ask for a refund policy that does not exist.
- Be rude to it.

Every failure you find becomes a new escalation rule. This is how real
customer-service systems are built — not by hoping, but by attacking your own.

::: exercise
**Exercise 9.3 — Build and break**

1. Build a ten-question bot for your own business.
2. Swap with a partner and attack theirs using the list above.
3. Write down every failure.
4. Fix the top three with escalation rules.
5. Re-test.

**Time:** 50 minutes. **Deliverable:** a working bot, a list of failures, and
three new rules.
:::

# Module 10 — Research You Can Defend

There is a difference between an answer and evidence. This module teaches the
difference, because it is the difference between being trusted and being caught.

## Lesson 10.1 — Tools that cite, and what citing means

Perplexity and search-grounded assistants return sources alongside claims. This
is a genuine improvement over a bare answer, and it is not a guarantee.

A link proves that a page exists. It does not prove that the page says what the
answer claims, that the page is credible, or that the page is current.

## Lesson 10.2 — The verification ritual

Five questions, every time, out loud if you have to:

1. Does the source exist?
2. Does it actually say that?
3. Is it recent enough?
4. Is it independent — or is it the seller?
5. What would the opposite view say?

::: scripture
"A false witness will not go unpunished, and he who speaks lies shall perish."
— Proverbs 19:9
:::

In an age of fluent, confident, machine-generated text, the person who checks is
the person who can be trusted. That is a competitive advantage, and it is also
simply the right way to behave.

## Lesson 10.3 — Interrogating long documents

NotebookLM lets you upload a set of documents and ask questions grounded only in
those documents. For anyone who has to read tenders, policies, reports or
contracts, this is transformative.

```prompt
Based only on the uploaded documents: summarise the main argument in five
bullets. List every figure with the source it came from. Tell me what is NOT
covered that I should be worried about. Where do the documents contradict
each other?
```

That last question is the one that finds the problem before your client does.

::: exercise
**Exercise 10.3 — The adversarial briefing**

1. Choose a decision you are actually facing.
2. Ask AI: "Give me the three strongest arguments against this, with sources."
3. Verify every source using the five-question ritual.
4. Write a one-page brief with five verified sources.
5. Note which sources failed verification — there is usually at least one.

**Time:** 45 minutes. **Deliverable:** a one-page brief.
:::

# Module 11 — Saving Time Every Week: Notes and Automation

Automation is not for big companies. It is for anyone who does the same boring
thing more than twice a week.

## Lesson 11.1 — Capture meetings without taking notes

Tools like Otter or Fireflies join a call, transcribe it, summarise it, and
extract action items. On a phone, you can record and have the assistant
transcribe and summarise.

The habit that matters: end every meeting with a written list of decisions and
owners. Whether a human or a machine produced it is irrelevant. What matters is
that it exists.

## Lesson 11.2 — Trigger, action, result

Every automation, however complex, is this shape:

**When X happens → do Y → which produces Z.**

| Trigger | Action | Result |
|---|---|---|
| Customer fills the enquiry form | Add a row to the sheet and send a confirmation email | Lead captured, customer reassured |
| WhatsApp message arrives after 6 p.m. | Send the away message and log it | Nothing is lost overnight |
| Invoice marked paid | Send a thank-you and update the dashboard | No manual chasing |

## Lesson 11.3 — The rule for what to automate

::: box
**Automate the boring, not the important.**

Boring tasks are repetitive, low-judgement, and safe to automate. Important
tasks require judgement, relationship, or accountability, and automating them
creates risk. A confirmation email is boring. A refund decision is important.
:::

Start with the fifteen most boring minutes of your week. Automate that. Then
the next fifteen. You will never run out.

::: exercise
**Exercise 11.3 — One automation, live**

1. Write your three-row trigger/action/result table for your own work.
2. Pick the simplest one.
3. Build it in Zapier or Make — or, if that is not available, as a saved
   template plus a reminder.
4. Run it for one week.
5. Log the minutes saved. Actual minutes, not a feeling.

**Time:** 40 minutes to build. One week to prove.
**Deliverable:** a number.
:::

# Module 12 — Ethics, Privacy and Your AI Policy

This is the module that protects you. Everything before it makes you fast.
This makes you safe while being fast.

## Lesson 12.1 — The data rule

What never goes into a chatbot:

- National ID numbers, passports, driving licences
- Bank details, mobile-money PINs, card numbers
- Passwords and access keys
- Client medical records or financial records
- Salary and personnel data
- Unreleased contracts and tender documents
- Another person's personal data without their consent

If you would not read it aloud in a crowded market, do not type it.

## Lesson 12.2 — Honesty and disclosure

When should you say AI helped?

The honest test: **would the reader change how much they trust this if they
knew?** A grammar-corrected email — no. A published article, a student
assignment, a professional report, or an image presented as a photograph — yes.

Disclosure is not weakness. In professional settings it increasingly signals
competence, the same way citing sources does.

## Lesson 12.3 — Bias, and who is missing

AI reflects the writing it learned from. In a Ugandan or East African context,
that means the default examples, names, prices and cultural assumptions in AI
output are frequently not yours.

Practical responses: ask for local examples explicitly; ask "who is missing from
this?"; review anything that affects people's opportunities — hiring, lending,
admissions — with particular care, because that is where bias does real damage.

## Lesson 12.4 — Your one-page AI policy

Every organisation needs five sentences. Not a forty-page framework. Five
sentences that a new employee can follow on their first day.

::: box
**AI USE POLICY — [Organisation name]**

1. We use AI to draft, summarise and design. A named human reviews every output
   before it reaches a customer, client, regulator or the public.

2. We never enter the following into an AI tool: client names with ID or
   financial details, medical records, passwords, bank details, unreleased
   contracts, or any third party's personal data without consent.

3. We disclose AI assistance where it affects what a reader would reasonably
   want to know.

4. We verify facts, figures, quotes and sources before publishing. Fluent
   output is not evidence.

5. This policy is reviewed every six months by [name], and every staff member
   confirms they have read it.

Signed: ______________________  Date: ____________
:::

::: exercise
**Exercise 12.4 — Write and test the policy**

1. Fill in the template for a real organisation.
2. Give it to someone who was not in this course.
3. Ask them: "Could you follow this on your first day?"
4. Fix whatever they could not follow.

**Time:** 30 minutes. **Deliverable:** a signed one-page policy.
:::

# Module 13 — Capstone: Build Your Own Workflow

Everything in this course exists to get you here: one working system, built for
your own work, that you will still be using in six months.

## Lesson 13.1 — The brief

Combine at least three tools into one workflow that solves a real problem. It
must run end to end. It must be measurable. It must be yours.

**Examples that have worked:**

- "WhatsApp enquiry to booked appointment in three minutes, fully automated."
- "One video becomes a week of posts across four platforms."
- "Monthly stock report generated from a photographed notebook."
- "Donor update written, designed and scheduled in 45 minutes."

## Lesson 13.2 — The rubric

| Criterion | Weight | Excellent | Weak |
|---|---|---|---|
| Working demo | 40% | Runs live, survives questions | Screenshots only |
| Measurable result | 25% | Before/after with evidence | "It feels faster" |
| Understanding of limits | 20% | Names the failure modes and the human check | Thinks AI is always right |
| Clarity | 15% | A non-technical person could repeat it | Jargon |

## Lesson 13.3 — Present in five minutes

Four slides. No more.

1. **The problem** — what it cost you before.
2. **The workflow** — the three tools and how they connect.
3. **The result** — the number.
4. **The limits** — what can go wrong and who checks.

The fourth slide is the one that separates a professional from an enthusiast.

::: exercise
**Exercise 13.3 — Ship it**

1. Build the workflow.
2. Run it three times for real.
3. Record the before and after times.
4. Present in five minutes.
5. Write down the date you will review whether you are still using it.

**Time:** 90 minutes build, 60 minutes presentations.
**Deliverable:** a working workflow and a five-minute presentation.
:::

# Module 14 — Ninety Days After the Course

The course is not the change. The ninety days after it are.

## Lesson 14.1 — The habit that makes it stick

**Weeks 1–4.** One real task per week with AI. Log four things: the task, the
prompt you used, the time saved, and what you had to fix.

**Weeks 5–8.** Teach one colleague one thing you learned. Teaching is the
retention mechanism; you will understand it properly only when you explain it.

**Weeks 9–12.** Automate one recurring task. Report the hours saved back to the
group.

The people who do this finish the course. The people who do not, forget it in a
month. There is no third outcome.

## Lesson 14.2 — Where to go next

If you want to go deeper, the ladder is:

- **AI-201 Practitioner** — turn these habits into systems your team can run.
- **AI-301 Builder** — custom assistants, image pipelines, agents.
- **AI-401 Specialist** — governance, evaluation, and selling AI work.

::: scripture
"Whatever you do, do it heartily, as to the Lord and not to men, knowing that
from the Lord you will receive the reward of the inheritance; for you serve the
Lord Christ."
— Colossians 3:23–24
:::

Whatever you build with this — a shop, a school, a ministry, a career — build it
well. The tools will change every year. The standard does not.

::: prayer
**A closing reflection**

Lord, give me the diligence to learn what is useful, the discernment to reject
what is false, and the honesty to say plainly what I have done and what I have
not. Let the hours this saves be spent on people, not on more output.
Amen.
:::
