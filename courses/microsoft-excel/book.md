# Module 1 — The Grid, and Why It Matters

A spreadsheet is a grid of cells, each with an address: column letter, row number.
C5 is column C, row 5. That address system is what makes formulas possible, and
formulas are what make a spreadsheet a tool rather than a table.

Most people use Excel as a place to type numbers. This course turns it into a
place to answer questions.

::: scripture
"The plans of the diligent lead surely to plenty, but those of everyone who is
hasty, surely to poverty."
— Proverbs 21:5
:::

Diligence in a spreadsheet looks like: building it once, properly, so that it works
every month without being rebuilt. Haste looks like typing numbers into a fresh
sheet every time and never knowing whether they add up.

## Lesson 1.1 — The interface

**The grid** — cells, rows, columns.
**The formula bar** — shows what is actually in the selected cell.
**The name box** — shows the address; type an address to jump there.
**Sheet tabs** — multiple sheets in one file.
**The status bar** — shows sum, average and count of a selection. Free, instant
answers.

## Lesson 1.2 — Data types

A cell holds one of four things, and the type matters:

**Number** — can be calculated. Right-aligned by default.
**Text** — cannot be calculated. Left-aligned by default.
**Date** — a number formatted as a date.
**Formula** — starts with `=`, calculates something.

The most common error: a number stored as text. It looks right, it is left-aligned,
and `=SUM` ignores it. The fix: Format Cells, or multiply by 1.

## Lesson 1.3 — Good habits from day one

- One table per sheet. Do not scatter.
- Header row with single-word column names, no spaces.
- No blank rows inside data.
- No merged cells inside data tables. Ever.
- One value per cell. Not "Kampala, 2 boxes".

These five habits prevent 80 percent of spreadsheet problems.

::: exercise
**Exercise 1.3 — Build a clean table**

1. Create a sheet with columns: Date, Item, Qty, UnitPrice, Total.
2. Enter 20 rows of realistic data.
3. Check every number is right-aligned (a number) not left-aligned (text).
4. Add a Total column with `=C2*D2` and fill down.
5. Select the Total column and read the sum in the status bar.

**Time:** 30 minutes. **Deliverable:** a clean, calculating table.
:::

# Module 2 — Formulas That Work

## Lesson 2.1 — The four operators

`+` add, `-` subtract, `*` multiply, `/` divide. Plus `^` for powers and `%` for
percentages.

Every formula starts with `=` and uses cell addresses, not typed numbers. `=B2*C2`
is a formula. `=500*3` is a calculation that will be wrong tomorrow.

## Lesson 2.2 — The functions you will actually use

| Function | Does | Example |
|---|---|---|
| SUM | Adds a range | `=SUM(E2:E50)` |
| AVERAGE | Mean | `=AVERAGE(E2:E50)` |
| COUNT | Counts numbers | `=COUNT(E2:E50)` |
| COUNTA | Counts non-blank | `=COUNTA(A2:A50)` |
| MAX / MIN | Largest / smallest | `=MAX(E2:E50)` |
| ROUND | Rounds | `=ROUND(E2,2)` |
| IF | Conditional | `=IF(E2>1000,"High","Low")` |
| SUMIF | Conditional sum | `=SUMIF(F2:F50,"Paid",E2:E50)` |
| COUNTIF | Conditional count | `=COUNTIF(F2:F50,"Paid")` |
| SUMIFS | Multiple conditions | `=SUMIFS(E2:E50,F2:F50,"Paid",B2:B50,"Rice")` |

SUMIFS is the workhorse of business reporting. Learn it properly.

## Lesson 2.3 — Absolute and relative references

`B2` is relative — it shifts when you copy the formula.
`$B$2` is absolute — it stays fixed.

Use `$` when referring to a fixed value, like a tax rate in a single cell. Copy a
formula with `B2` when you want it to move down the column.

## Lesson 2.4 — Debugging formulas

Four steps, always in this order:

1. **Read the error.** `#DIV/0!` means division by zero. `#VALUE!` means text where
   a number was expected. `#REF!` means a deleted cell. `#N/A` means a lookup failed.
2. **Click the cell and read the formula bar.** Most errors are visible there.
3. **Use Evaluate Formula** (Formulas → Evaluate Formula) to step through.
4. **Test one part at a time.** Build the formula in pieces.

::: exercise
**Exercise 2.4 — Build a summary**

1. From your 20-row table, calculate: total revenue, average sale, highest sale,
   number of transactions.
2. Add a Paid column with Yes/No values.
3. Use SUMIF to total only paid amounts.
4. Use COUNTIF to count unpaid transactions.
5. Break one formula deliberately and read the error message.

**Time:** 40 minutes. **Deliverable:** a summary block with five calculations.
:::

# Module 3 — Lookups

## Lesson 3.1 — What a lookup does

A lookup takes a value, finds it in another table, and returns something from the
same row. In practice: "given this product code, what is the price?"

## Lesson 3.2 — VLOOKUP and XLOOKUP

`=VLOOKUP(A2, Prices!$A$2:$B$100, 2, FALSE)`

Reads as: find A2 in the first column of the Prices table, return the value from
column 2, exact match only.

Three rules that prevent most VLOOKUP failures:

1. Always use `FALSE` for exact match. `TRUE` gives approximate matches and silent
   errors.
2. Always use `$` on the table range, or it will shift when copied.
3. The lookup value must be in the **first** column of the table.

XLOOKUP, in newer versions, is better: it can look left or right, and it handles
missing values gracefully.

`=XLOOKUP(A2, Prices!$A$2:$A$100, Prices!$C$2:$C$100, "Not found")`

## Lesson 3.3 — INDEX and MATCH

The classic alternative that works in every version:

`=INDEX(Prices!$C$2:$C$100, MATCH(A2, Prices!$A$2:$A$100, 0))`

It looks complicated and is more flexible: the return column can be anywhere.

::: warn
**The silent VLOOKUP disaster.** If a lookup value has a trailing space, or a
number is stored as text, VLOOKUP returns `#N/A` and people conclude the data is
missing. Check with `=LEN(A2)` and `=ISNUMBER(A2)` before rebuilding anything.
:::

::: exercise
**Exercise 3.3 — Price lookup**

1. Create a second sheet with a price list: Code, Description, Price.
2. In your main table, add a Price column populated by VLOOKUP from the code.
3. Copy it down 20 rows. Check three random results by hand.
4. Deliberately add a trailing space to one code and observe the error.
5. Fix it with TRIM.

**Time:** 45 minutes. **Deliverable:** a working lookup with a fixed edge case.
:::

# Module 4 — Cleaning Messy Data

## Lesson 4.1 — The five common problems

1. **Inconsistent text** — "Yes", "yes", "YES".
2. **Trailing spaces** — invisible, breaks lookups.
3. **Duplicates** — the same customer entered twice.
4. **Numbers as text** — cannot be summed.
5. **Inconsistent dates** — 03/04/2026 and 3 April 2026 in the same column.

## Lesson 4.2 — The cleaning toolkit

| Function | Fixes |
|---|---|
| `TRIM()` | Leading and trailing spaces |
| `PROPER()` / `UPPER()` / `LOWER()` | Case consistency |
| `VALUE()` | Text to number |
| `TEXT()` | Number to formatted text |
| `LEFT()`, `RIGHT()`, `MID()` | Extract part of a value |
| `LEN()` | Check for hidden characters |
| Remove Duplicates | Data tab → Remove Duplicates |

## Lesson 4.3 — The safe workflow

**Always work on a copy.** Keep the original sheet untouched. Clean in a new
sheet, then verify, then replace.

The verification step: compare row counts and totals before and after. If the total
changed, something was lost.

::: exercise
**Exercise 4.3 — Clean a messy sheet**

1. Create a deliberately messy table: inconsistent case, trailing spaces,
   duplicates, some numbers as text.
2. Clean it using TRIM, PROPER and Remove Duplicates.
3. Convert text-numbers using VALUE.
4. Compare the row count and total before and after.
5. Write down what changed and why.

**Time:** 45 minutes. **Deliverable:** a clean table and a before/after comparison.
:::

# Module 5 — Pivot Tables

## Lesson 5.1 — What a pivot table is for

It summarises a large table by category. "Total sales by product by month" from a
thousand rows, in about thirty seconds, without a single formula.

## Lesson 5.2 — Building one

1. Click anywhere in your data.
2. Insert → PivotTable → New Worksheet.
3. Drag fields into four areas:
   - **Rows** — what you want to group by (Product).
   - **Columns** — the second grouping (Month).
   - **Values** — what you want to measure (Sum of Total).
   - **Filters** — optional (Region).

## Lesson 5.3 — The settings that matter

- **Change the calculation** from Count to Sum (Excel often guesses Count).
- **Number format** — set currency, or your totals will look wrong.
- **Show values as** — percentage of total, percentage of column, running total.
- **Group dates** — right-click a date field to group by month or quarter.
- **Refresh** — a pivot table does not update automatically. Right-click → Refresh.

## Lesson 5.4 — The one-page dashboard

Four pivot tables and four charts on one sheet, with a slicer to filter them all
at once. Insert → Slicer. Click it, and everything updates.

That is a dashboard, and it takes about forty minutes.

::: exercise
**Exercise 5.4 — Build a dashboard**

1. From your 20-row table, build a pivot: total by Item.
2. Build a second: total by Month.
3. Add a chart to each.
4. Add a slicer for the Paid column.
5. Arrange them on one sheet with a title.

**Time:** 50 minutes. **Deliverable:** a one-page dashboard.
:::

# Module 6 — Charts That Say Something

## Lesson 6.1 — Which chart for which question

| Question | Chart |
|---|---|
| How does this change over time? | Line |
| How do categories compare? | Bar or column |
| What proportion of the whole? | Pie — only with 2–5 slices |
| Is there a relationship between two numbers? | Scatter |
| What is the distribution? | Histogram |

Most bad charts are a pie with twelve slices answering a question a bar chart would
answer better.

## Lesson 6.2 — Chart discipline

- One message per chart. Put the message in the title.
- Label both axes, with units.
- Remove gridlines and legends you do not need.
- Start the y-axis at zero for bar charts. Truncating the axis exaggerates.
- Sort the bars. Unsorted bars are harder to read than sorted ones.

::: exercise
**Exercise 6.2 — Fix a bad chart**

1. Create a pie chart with twelve categories.
2. Note how unreadable it is.
3. Rebuild it as a sorted bar chart.
4. Write a title that states the finding, not the data.
5. Show both to someone and ask which they understood faster.

**Time:** 30 minutes. **Deliverable:** a before-and-after pair.
:::

# Module 7 — Automating Recurring Work

## Lesson 7.1 — What to automate

Anything you do monthly with the same structure. Reports, reconciliations, invoice
registers.

## Lesson 7.2 — The tools

**Tables** (Ctrl+T) — expand automatically when you add rows, and formulas fill
down.

**Named ranges** — refer to a range by name instead of address.

**Data validation** — restrict a cell to a list, a number range, or a date. Prevents
typos at the source, which is better than fixing them later.

**Conditional formatting** — highlight overdue invoices, negative margins, duplicate
entries. Rules that do the checking for you.

**Templates** — save a workbook as a template so next month starts from a clean,
correct structure.

## Lesson 7.3 — The monthly report that builds itself

Structure: a raw data sheet, a pivot table, a dashboard sheet. Each month, paste
new data into the raw sheet, refresh the pivot, and the dashboard updates.

That is a report that takes five minutes instead of five hours.

::: exercise
**Exercise 7.3 — Build the template**

1. Convert your data range to a Table (Ctrl+T).
2. Add data validation to the Paid column (Yes/No list).
3. Add conditional formatting to highlight unpaid rows.
4. Build the pivot and dashboard on separate sheets.
5. Save as a template. Use it next month.

**Time:** 60 minutes. **Deliverable:** a reusable monthly report template.
:::

# Module 8 — AI in Excel

## Lesson 8.1 — What it does well

Writing formulas from a plain-English description, explaining a formula you
inherited, suggesting a chart, and summarising a data range in words.

## Lesson 8.2 — What it does badly

Arithmetic on large ranges, and anything involving a specific cell reference it
cannot see. It will produce a formula that looks right and references the wrong
column.

## Lesson 8.3 — The safe pattern

1. Describe the calculation in plain English, including the exact columns.
2. Ask for the formula **and** an explanation of each part.
3. Test it on three rows where you know the answer.
4. Only then fill it down.

```prompt
In Excel, column E should be quantity in C multiplied by unit price in D,
rounded to two decimals. Write the formula for E2 and explain each part in
one sentence.
```

::: warn
**Never let AI do the arithmetic and never trust a total you have not checked.**
Use AI to write the formula; use the spreadsheet to calculate. The spreadsheet is
right, and it can be audited. A language model's mental arithmetic cannot.
:::

::: exercise
**Exercise 8.3 — Formula by description**

1. Choose a calculation you find difficult.
2. Describe it to AI with exact column letters.
3. Get the formula and the explanation.
4. Test on three known rows.
5. Save the prompt to your library.

**Time:** 25 minutes. **Deliverable:** a working formula you understand.
:::

# Module 9 — Capstone

## Lesson 9.1 — The brief

Build a workbook with: a clean data sheet, at least six formulas including a
lookup and a SUMIFS, a pivot table, two charts, a one-page dashboard, data
validation, conditional formatting, and a template version saved for next month.

## Lesson 9.2 — The rubric

| Criterion | Weight | Excellent | Weak |
|---|---|---|---|
| Data structure | 25% | Clean table, no merged cells, one value per cell | Scattered, inconsistent |
| Formulas | 30% | Correct, readable, tested | Hard-coded numbers |
| Analysis | 20% | Pivot answers a real question | Pivot with wrong aggregation |
| Presentation | 15% | Dashboard readable at a glance | Chart soup |
| Reusability | 10% | Works next month with new data | Rebuilt from scratch |

::: scripture
"A false balance is an abomination to the Lord, but a just weight is His delight."
— Proverbs 11:1
:::

A spreadsheet is a set of scales. It will tell you the truth about your business
whether or not you want to hear it — which is precisely why it is worth learning
properly.

::: prayer
**A closing reflection**

Lord, give me the patience to build things correctly the first time, and the
honesty to look at numbers that do not flatter me. Let my accounts be true.
Amen.
:::
