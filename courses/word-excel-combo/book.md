# Module 1 — The Pair That Runs the Office

Word and Excel are taught separately in most courses, and then the same learner
discovers that every real task uses both. A report is a Word document containing
an Excel table. A certificate is a Word template filled from an Excel list. A
quotation is a Word letter with figures calculated in Excel.

This course teaches them together, in the order work actually arrives.

::: scripture
"Two are better than one, because they have a good reward for their labour."
— Ecclesiastes 4:9
:::

Two tools, one workflow. That is the whole design of this course.

## Lesson 1.1 — The division of labour

**Word handles language.** Prose, letters, reports, policies, contracts.

**Excel handles numbers.** Calculations, lists, totals, comparisons, charts.

The mistake is using one to do the other's job: building tables in Word (which
cannot calculate) or writing paragraphs in Excel (which cannot wrap text
sensibly).

## Lesson 1.2 — The five tasks this course covers

1. A professional letter, correctly formatted.
2. A spreadsheet that calculates.
3. A report with a live table from Excel.
4. A mail merge from Excel into Word.
5. A combined document with an embedded chart.

That is 90 percent of office work.

## Lesson 1.3 — Habits that apply to both

- Save constantly. Ctrl+S is a reflex, not a decision.
- Name files by date and subject.
- Keep one folder per project.
- Never work in a file you cannot find again.

::: exercise
**Exercise 1.3 — Set up your workspace**

1. Create a folder called "Office Course".
2. Inside it, create: Letters, Sheets, Reports, Merges.
3. Create one blank Word document and one blank Excel workbook in the correct
   folders.
4. Save both with the date-subject naming pattern.
5. Note the shortcuts: Ctrl+S, Ctrl+Z, Ctrl+C, Ctrl+V, Ctrl+H.

**Time:** 15 minutes. **Deliverable:** an organised workspace.
:::

# Module 2 — Word: Documents That Look Professional

## Lesson 2.1 — Styles, not formatting

Apply Heading 1, Heading 2, and Normal. Do not make text bold and large by hand.

Why: styles let you change every heading at once, they create a navigable outline,
and they enable an automatic table of contents. Everything else in Word depends on
them.

## Lesson 2.2 — The professional letter

Structure: sender details, date, recipient, subject line, greeting, body, close,
signature.

Formatting: one font, size 11 or 12, 2.5 cm margins, single or 1.15 line spacing,
left-aligned (not justified — justified text creates ugly gaps).

## Lesson 2.3 — Tables in Word

Insert → Table. Set the column widths by dragging borders. Turn off "Allow row to
break across pages" in Table Properties. Repeat the header row if the table spans
pages.

Remember: a Word table cannot calculate. If you need arithmetic, the table belongs
in Excel.

## Lesson 2.4 — Page numbers and headers

Insert → Page Number → Bottom of Page. Then set "Different First Page" so a cover
page has no number.

::: exercise
**Exercise 2.4 — Write a real letter**

1. Write a formal letter requesting something you actually need.
2. Use one font, 2.5 cm margins, correct spacing.
3. Add a subject line.
4. Save as both DOCX and PDF.
5. Read it aloud. Fix anything that sounds wrong when spoken.

**Time:** 30 minutes. **Deliverable:** a letter and a PDF.
:::

# Module 3 — Excel: Numbers That Calculate

## Lesson 3.1 — The essential formulas

`=B2*C2` multiplies. `=SUM(E2:E20)` totals. `=AVERAGE(E2:E20)` averages.
`=IF(E2>1000,"High","Low")` decides.

Always reference cells. Never type a number into a formula.

## Lesson 3.2 — Formatting that helps

- Currency format on money columns.
- Two decimal places on prices.
- Date format on dates.
- Bold the header row.
- Freeze the header row (View → Freeze Panes).

## Lesson 3.3 — The table that will go into Word

Build it cleanly: header row, one value per cell, no merged cells, totals at the
bottom. This is the table you will copy into your report.

## Lesson 3.4 — Charts

Select the data, Insert → Chart, choose the type. Then simplify: delete gridlines,
add data labels, write a title that states the finding.

::: exercise
**Exercise 3.4 — Build the source table**

1. Create a sheet: Item, Qty, UnitPrice, Total.
2. Add 12 rows of realistic data.
3. Add a Total column with a formula.
4. Add a total row with `=SUM`.
5. Format as currency. Freeze the header. Add a bar chart.

**Time:** 35 minutes. **Deliverable:** a clean calculating table with a chart.
:::

# Module 4 — Linking Excel Into Word

## Lesson 4.1 — Three ways to get Excel data into Word

| Method | Behaviour | Use when |
|---|---|---|
| **Copy and Paste** | Static table | Data will not change |
| **Paste Special → Link** | Updates when Excel changes | Data changes regularly |
| **Insert → Object** | Embedded file, editable in place | You need the whole workbook |

## Lesson 4.2 — Paste Special, properly

In Excel: copy the range. In Word: Home → Paste → Paste Special → "Microsoft Excel
Worksheet Object" → Paste Link.

Now the Word table updates when the Excel file changes. Right-click → Update Link
refreshes it manually; File → Options → Advanced controls automatic updating.

## Lesson 4.3 — Formatting a linked table

A linked table inherits Excel's formatting, which is often not what you want in a
document. Fix it in Excel, not in Word — changes in Word are overwritten on update.

This is the single most important thing to understand about linked tables.

## Lesson 4.4 — The embedded chart

Copy a chart in Excel, paste into Word with Paste Special → Link. It updates with
the data.

::: warn
**Broken links.** A linked table points to a specific file path. If you move or
rename the Excel file, the link breaks. Keep linked files in the same folder as the
Word document, and never rename them after linking.
:::

::: exercise
**Exercise 4.4 — Link a table and a chart**

1. Copy your Excel table into Word using Paste Special → Paste Link.
2. Change a number in Excel. Update the link in Word. Confirm it changed.
3. Copy the chart the same way.
4. Move the Excel file and observe the broken link.
5. Move it back and repair the link.

**Time:** 40 minutes. **Deliverable:** a Word document with live linked data.
:::

# Module 5 — Mail Merge

## Lesson 5.1 — The three parts

**The data** — an Excel sheet, one row per recipient, single-word column headers.

**The template** — a Word document with merge fields.

**The connection** — Mailings → Start Mail Merge → Select Recipients.

## Lesson 5.2 — Building the data

| Name | Amount | DueDate | Course |
|---|---|---|---|
| Nakato Sarah | 150000 | 2026-04-15 | Graphic Design |
| Mukasa Peter | 200000 | 2026-04-15 | AI Foundation |

Rules: no blank rows, no merged cells, headers with no spaces, dates in a
consistent format.

## Lesson 5.3 — Building the template

Write the letter normally. Where a value goes, insert a merge field:
Mailings → Insert Merge Field → Name.

It appears as `«Name»`. That is correct.

## Lesson 5.4 — Preview and finish

Preview Results, then click through at least three records. Errors hide in record
two.

Finish & Merge → Edit Individual Documents, then check the merged output before
printing.

## Lesson 5.5 — Certificates

The highest-value merge in a school or training institution: 200 certificates from
one template and one spreadsheet. Use a landscape page, a border image, and three
merge fields: name, course, date.

::: exercise
**Exercise 5.5 — Merge 20 letters**

1. Build the Excel data with 20 rows.
2. Write the Word letter with three merge fields.
3. Connect, preview three records, merge.
4. Save the merged document.
5. Repeat the same data as certificates in landscape.

**Time:** 60 minutes. **Deliverable:** 20 letters and 20 certificates.
:::

# Module 6 — The Report With Everything

## Lesson 6.1 — Structure

1. Cover page — title, author, date, organisation.
2. Table of contents — automatic, from styles.
3. Introduction — what this is and why.
4. Findings — the body, with tables and charts.
5. Conclusion — what it means.
6. Recommendations — what to do.
7. Appendix — detail for the curious.

## Lesson 6.2 — Assembling it

Write in Word. Insert tables and charts from Excel as links. Apply Heading styles
throughout. Generate the table of contents. Add page numbers.

## Lesson 6.3 — The finishing checks

- Update the table of contents.
- Check every figure against the source.
- Check page breaks — no heading stranded at the bottom of a page.
- Export to PDF and read it on a phone.

::: exercise
**Exercise 6.3 — Build the report**

1. Write a four-page report on something you actually know.
2. Include at least two linked tables and one linked chart.
3. Add a cover page and an automatic table of contents.
4. Add page numbers, with no number on the cover.
5. Export to PDF and check on two devices.

**Time:** 75 minutes. **Deliverable:** a complete report.
:::

# Module 7 — Speed and Consistency

## Lesson 7.1 — Word shortcuts worth learning

| Shortcut | Action |
|---|---|
| Ctrl+H | Find and replace |
| Ctrl+Enter | Page break |
| Ctrl+Shift+C / V | Copy / paste formatting |
| F4 | Repeat last action |
| Ctrl+Alt+1 / 2 / 3 | Apply Heading 1 / 2 / 3 |

F4 is the hidden gem: apply a format once, then press F4 to repeat it.

## Lesson 7.2 — Excel shortcuts worth learning

| Shortcut | Action |
|---|---|
| Ctrl+; | Insert today's date |
| Ctrl+Shift+L | Toggle filters |
| Alt+= | AutoSum |
| F2 | Edit the cell |
| Ctrl+Arrow | Jump to the edge of data |
| Ctrl+Shift+Arrow | Select to the edge |

## Lesson 7.3 — Templates

Save your best letter, report and invoice as templates (.dotx / .xltx). Next time,
start from a correct structure instead of a blank page.

::: exercise
**Exercise 7.3 — Build three templates**

1. A letter template with your details pre-filled.
2. A report template with the heading styles and a table of contents.
3. An invoice template with formulas in Excel.

**Time:** 45 minutes. **Deliverable:** three templates.
:::

# Module 8 — AI in Both Tools

## Lesson 8.1 — Where it helps

**Word:** drafting, rewriting at a different length or tone, summarising, suggesting
structure.

**Excel:** writing formulas from a description, explaining a formula, suggesting a
chart type.

## Lesson 8.2 — Where it fails

Numbers. Every time. An AI can write a formula but its arithmetic is unreliable,
and a wrong total in a quotation is a real financial loss.

The rule: **let AI write the formula, let Excel do the calculation, and check the
result against a known row.**

## Lesson 8.3 — The workflow

```prompt
In Excel, column D should be quantity in B multiplied by price in C, rounded
to whole shillings. Write the formula for D2 and explain each part.
```

Then test on three rows where you know the answer. Only then fill down.

::: exercise
**Exercise 8.3 — Formula and draft**

1. Describe a calculation to AI, with exact column letters.
2. Get the formula, test it on three known rows.
3. Ask AI to draft the introduction to your report.
4. Rewrite the draft in your own words.
5. Check every number in the final document against the spreadsheet.

**Time:** 35 minutes. **Deliverable:** a tested formula and a rewritten draft.
:::

# Module 9 — Capstone

## Lesson 9.1 — The brief

Produce a complete office package: a formal letter, a calculating spreadsheet, a
report with two linked tables and one linked chart, a mail merge of ten records,
and an automatic table of contents — all exported to PDF.

## Lesson 9.2 — The rubric

| Criterion | Weight | Excellent | Weak |
|---|---|---|---|
| Word craft | 25% | Styles, clean layout, correct numbering | Manual formatting |
| Excel craft | 25% | Formulas, formatting, correct totals | Typed numbers |
| Integration | 25% | Links work and update | Static copy-paste |
| Merge | 15% | Ten correct personalised documents | Manual duplication |
| Finishing | 10% | PDF checked, TOC updated | Untested export |

::: scripture
"Whatever you do, do it heartily, as to the Lord and not to men."
— Colossians 3:23
:::

The pair of Word and Excel is unglamorous and it is the language of offices
everywhere. Someone who can produce a clean report with live data is quietly
indispensable — and quietly employable.

::: prayer
**A closing reflection**

Lord, let my documents be accurate and my numbers true. Let the work I hand over
be something I would be content to sign my name to. Amen.
:::
