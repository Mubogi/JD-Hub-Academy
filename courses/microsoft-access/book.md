# Module 1 — When Excel Stops Coping

Excel is extraordinary. It is also a flat sheet of paper pretending to be a
database, and eventually it breaks: duplicate customers, inconsistent spellings,
no way to enforce that a phone number is a phone number, and a file that takes
four minutes to open.

Access is what you use when the answer to "how do these things relate?" matters
more than "what is the total?"

::: scripture
"Let all things be done decently and in order."
— 1 Corinthians 14:40
:::

Order in data means one fact stored once. Everything in this course follows from
that single rule.

## Lesson 1.1 — The signals that you need a database

- You have the same customer name typed six different ways.
- You have three spreadsheets that must be kept in sync by hand.
- You cannot answer "which members have loans over 90 days and also missed two
  savings deposits?" without an hour of manual work.
- You have a column where some cells contain two values ("Kampala, 2 boxes").
- More than one person needs to enter data.

Any two of those and you need a database.

## Lesson 1.2 — What a relational database is

Tables hold data. Each table holds one kind of thing: Members, Loans, Payments.

**Records** are rows — one member, one loan.
**Fields** are columns — name, amount, date.
**Primary key** is a unique identifier for each record.
**Foreign key** is a reference to a record in another table.

The power comes from the last two: a loan record does not repeat the member's
name and phone number. It stores the member's ID. The name lives once, in the
Members table.

## Lesson 1.3 — The four objects in Access

| Object | Purpose |
|---|---|
| **Table** | Where data lives |
| **Query** | A question asked of the data |
| **Form** | A screen for entering data |
| **Report** | A printable output |

Everything in this course is one of those four.

::: exercise
**Exercise 1.3 — Model on paper**

1. Choose a process you manage: members, stock, clients, patients.
2. List the things involved (people, items, transactions).
3. For each, list its attributes.
4. Draw the tables as boxes, with the primary key underlined.
5. Draw lines between tables where one refers to another.

**Time:** 40 minutes. **Deliverable:** a paper data model. Do not open Access yet.
:::

# Module 2 — Table Design

## Lesson 2.1 — One table, one subject

A table should hold one kind of thing. If a table holds members *and* their loans,
it is two tables wearing one coat, and every loan will duplicate the member's
details.

## Lesson 2.2 — Field types

| Type | Use | Note |
|---|---|---|
| Short Text | Names, codes, phone numbers | Phone numbers are text, not numbers |
| Number | Quantities, amounts | Set the format |
| Currency | Money | Set the decimal places |
| Date/Time | Dates | Always use this, never text |
| Yes/No | True/false flags | |
| AutoNumber | Primary key | Automatic unique ID |
| Lookup | A value from another table | Creates the relationship |

## Lesson 2.3 — The rules that prevent pain

- Every table has an AutoNumber primary key.
- Every field has the correct type. A date stored as text cannot be sorted.
- Set field sizes. Short Text defaults to 255 characters; use less.
- Set required fields. A member with no name is a bug.
- Use validation rules where possible. `>=0` on an amount prevents negatives.
- Add a description to each field. Future-you will need it.

## Lesson 2.4 — Normalisation, in plain language

Three rules, and you do not need the formal names:

1. **One value per cell.** Not "Kampala, 2 boxes".
2. **One fact in one place.** A member's phone number appears once, in the
   Members table.
3. **No repeating groups.** Do not have Phone1, Phone2, Phone3. Have a separate
   table.

::: warn
**The most expensive mistake in Access** is designing the tables badly and then
trying to fix it after entering data. Design on paper, review it, and only then
build. Changing a table's structure after it holds data means rebuilding the
queries, forms and reports that depend on it.
:::

::: exercise
**Exercise 2.4 — Build three tables**

1. Create a table: Members (MemberID AutoNumber, FirstName, LastName, Phone,
   JoinDate).
2. Create a table: Loans (LoanID AutoNumber, MemberID Number, Amount Currency,
   DateIssued Date, Status Short Text).
3. Create a table: Payments (PaymentID AutoNumber, LoanID Number, Amount
   Currency, DatePaid Date).
4. Set the field types and validation rules.
5. Enter five members, five loans, five payments.

**Time:** 50 minutes. **Deliverable:** three related tables with data.
:::

# Module 3 — Relationships

## Lesson 3.1 — Why relationships matter

Without a relationship, a query cannot combine tables. With one, you can ask "which
member has this loan?" and get an answer in a second.

## Lesson 3.2 — The three relationship types

**One-to-many.** One member has many loans. The most common, and the one you will
use.

**One-to-one.** One member has one membership card. Rare.

**Many-to-many.** Many students take many courses. Requires a third "joining"
table.

## Lesson 3.3 — Referential integrity

This setting enforces two rules:

1. You cannot add a loan for a member who does not exist.
2. You cannot delete a member who has loans.

That second rule has saved more databases than any other feature. Without it,
deleting one member orphans their loans and silently corrupts your reports.

Turn it on. Always.

::: exercise
**Exercise 3.3 — Create the relationships**

1. Database Tools → Relationships.
2. Add all three tables.
3. Drag MemberID from Members onto MemberID in Loans.
4. Drag LoanID from Loans onto LoanID in Payments.
5. Enforce referential integrity on both.

**Time:** 30 minutes. **Deliverable:** three tables joined correctly.
:::

# Module 4 — Queries

## Lesson 4.1 — The query designer

Create → Query Design. Add tables. Drag fields into the grid. Run.

That is a select query, and it is the workhorse.

## Lesson 4.2 — The four kinds

**Select** — retrieves data. The default.
**Parameter** — asks for a value each time it runs.
**Action** — changes data (update, append, delete).
**Totals** — groups and calculates.

## Lesson 4.3 — Criteria

| Criterion | Meaning |
|---|---|
| `"Kampala"` | Equals Kampala |
| `>"2026-01-01"` | After that date |
| `Between 1000 And 5000` | In range |
| `Is Null` | Empty |
| `Like "M*"` | Starts with M |
| `<>"Paid"` | Not paid |

## Lesson 4.4 — Totals queries

Design → Totals (the sigma button). Then choose: Group By, Sum, Count, Average,
Max, Min.

"Total loan amount by status" is three drags and one dropdown. In Excel, that is a
pivot table rebuilt every month.

## Lesson 4.5 — Calculated fields

`Total: [Amount] * 1.1`

In a query, a calculated field is written `FieldName: expression`. It calculates
on the fly and does not store the result — which is correct, because stored
calculations go out of date.

::: exercise
**Exercise 4.5 — Four queries**

1. **Select:** all loans over 500,000.
2. **Parameter:** ask for a member ID and show their loans.
3. **Totals:** total loan amount by status.
4. **Calculated:** outstanding balance, assuming no payments, with a 10 percent
   fee added.

**Time:** 60 minutes. **Deliverable:** four working queries.
:::

# Module 5 — Forms

## Lesson 5.1 — Why forms

A table grid is fine for you and dangerous for a data-entry clerk. A form controls
what can be entered, in what order, with what validation.

## Lesson 5.2 — The form wizard

Create → Form Wizard. Choose the table, choose the fields, choose a layout. Thirty
seconds.

Then improve it: move fields, resize, add a title, add a subform for related
records.

## Lesson 5.3 — Subforms

A form showing a member, with a subform showing all their loans, is the single most
useful Access screen in a small organisation. It shows the whole relationship on
one page.

Create it with the wizard: choose the main table, then the related table, and tick
"Subform".

## Lesson 5.4 — Comboboxes and validation

Replace a free-text field with a dropdown (a combobox) and you eliminate the
spelling variation problem entirely. A list of statuses — Applied, Approved,
Disbursed, Repaid, Defaulted — means every record uses the same vocabulary.

::: exercise
**Exercise 5.4 — Build a member form**

1. Create a form for Members with all fields.
2. Add a subform for their Loans.
3. Convert the Status field to a combobox with five values.
4. Set the form's record source correctly.
5. Enter three members and their loans through the form only.

**Time:** 50 minutes. **Deliverable:** a working member form with a subform.
:::

# Module 6 — Reports

## Lesson 6.1 — Why reports are separate from queries

A query answers a question. A report presents the answer: grouped, formatted,
totalled, with headers and footers, ready to print or send to a board.

## Lesson 6.2 — The report wizard

Create → Report Wizard. Choose the table or query, choose grouping, choose sorting,
choose layout. Then improve in Design View.

## Lesson 6.3 — Grouping and totals

Group by Member, and each member's loans appear together with a subtotal. Group by
month, and you get a monthly statement.

Add a report footer for the grand total. Add a page footer for the date and page
number.

## Lesson 6.4 — The reports a small organisation needs

| Report | Grouped by | Totals |
|---|---|---|
| Member statement | Member | Balance |
| Monthly loan disbursement | Month | Amount |
| Arrears list | Days overdue | Outstanding |
| Stock reorder | Supplier | Quantity |

::: exercise
**Exercise 6.4 — Build two reports**

1. A member statement: grouped by member, showing loans and payments, with a
   balance.
2. A monthly summary: grouped by month, with a total disbursed.

**Time:** 60 minutes. **Deliverable:** two printable reports.
:::

# Module 7 — Macros and Navigation

## Lesson 7.1 — Macros without code

A macro is a saved action. In Access, most macros are simple: open a form, open a
report, run a query, show a message.

Create → Macro. Choose an action from the dropdown. Save. Attach it to a button.

## Lesson 7.2 — The navigation form

Create → Navigation → Horizontal Tabs. Add buttons for each form and report. Now
the database opens onto a menu, and users never see the object list.

This single feature is what turns a collection of tables into something that looks
like an application.

## Lesson 7.3 — The startup settings

File → Options → Current Database. Set the display form to your navigation form,
and untick "Display Navigation Pane" and "Use Access Special Keys".

Now the database opens like an application, and a user cannot accidentally delete
a table.

::: exercise
**Exercise 7.3 — Build the menu**

1. Create a navigation form with tabs for Members, Loans, and two reports.
2. Add buttons that open each object.
3. Set it as the startup display form.
4. Hide the navigation pane.
5. Close and reopen the database. It should open as an application.

**Time:** 45 minutes. **Deliverable:** a database that opens as an application.
:::

# Module 8 — Compacting, Backing Up, Sharing

## Lesson 8.1 — Compact and repair

Access files grow as records are added and deleted. Compact and Repair (Database
Tools) shrinks the file and fixes minor corruption.

Do it weekly. A database that takes thirty seconds to open is a database that is
about to fail.

## Lesson 8.2 — Backing up

Copy the file. Daily. To a different drive or to cloud storage.

An Access database is a single file. If that file is corrupted and there is no
backup, everything is gone. This is not a theoretical risk; it happens routinely.

## Lesson 8.3 — Sharing, and the limits

Access is not designed for many simultaneous users over a network. Two or three
users on a wired local network is realistic. Ten users over Wi-Fi will corrupt it.

If you need more, you need a server database — which is a different conversation,
and a good problem to have.

::: warn
**Never put an Access database on a shared cloud folder** (Dropbox, OneDrive,
Google Drive) and let several people open it. The synchronisation will corrupt the
file. This is the single most common way small organisations lose their data.
:::

::: exercise
**Exercise 8.3 — Protect the database**

1. Compact and repair.
2. Create a backup copy in a different folder, named with today's date.
3. Write your backup routine: when, where, who.
4. Set the file to open in a specific folder.
5. Test: restore from the backup and confirm the data is intact.

**Time:** 30 minutes. **Deliverable:** a tested backup.
:::

# Module 9 — Capstone

## Lesson 9.1 — The brief

Build a working database application with: at least three related tables, two
forms including one with a subform, four queries including a totals query, two
reports, a navigation form, and a tested backup routine.

## Lesson 9.2 — The rubric

| Criterion | Weight | Excellent | Weak |
|---|---|---|---|
| Design | 30% | Normalised, correct types, no duplication | One big table |
| Relationships | 20% | Enforced referential integrity | Unlinked tables |
| Queries | 20% | Four types, correct criteria | Select only |
| Forms & reports | 20% | Usable, validated, printable | Default wizards unchanged |
| Operations | 10% | Compacted, backed up, tested | No backup |

::: scripture
"By wisdom a house is built, and by understanding it is established."
— Proverbs 24:3
:::

A well-built database is a house for your organisation's memory. Built badly, it
is a house that will collapse the day you are not there to hold it up.

::: prayer
**A closing reflection**

Lord, give me the patience to design before I build, and the foresight to prepare
for the day someone else must maintain what I made. Let my work be a foundation,
not a dependency.
Amen.
:::
