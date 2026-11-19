"""Cohort scheduling: intakes, ladder paths, capacity and booking windows.

The business manual fixes four intakes a year (February, May, August,
November) and a break-even of seven learners. This module turns that rhythm
into concrete dates and checks the one rule with commercial teeth: the ladder
discount requires a learner to start the next tier within 60 days of
finishing the previous one.

Run directly to print the schedule and the ladder check:
    python3 scripts/calendar_plan.py
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date, timedelta

from catalogue import COURSES

MIN_TO_RUN = 7
MAX_INDIVIDUAL = 12
MAX_CORPORATE = 15
LADDER_WINDOW = 60

INTAKE_MONTHS = (2, 5, 8, 11)
YEARS = (2026, 2027)

LADDER = ("ai-foundation", "ai-practitioner", "ai-builder", "ai-specialist")

# Non-ladder courses spread across the four intakes so no month is overloaded.
ROTATION = (
    ("digital-literacy", "graphic-design", "microsoft-office-suite"),
    ("digital-marketing", "financial-sacco", "practical-stem"),
    ("business-growth", "content-creation", "scratch-coding"),
    ("microsoft-office-suite", "graphic-design"),
)

# Start any Monday there are six enrolled.
ROLLING = (
    "microsoft-word",
    "microsoft-excel",
    "microsoft-powerpoint",
    "microsoft-access",
    "word-excel-combo",
)

# No cohort; read on your own schedule.
SELF_PACED = ("leadership",)

# Time slots. Two cohorts can share an intake only if they sit in different
# slots, because one facilitator cannot run two rooms at once. Evening slots
# suit working adults; the Saturday slot suits school-age courses.
SLOTS = (
    ("Mon + Wed, 18:00-20:00", "evening-a"),
    ("Tue + Thu, 18:00-20:00", "evening-b"),
    ("Sat, 09:00-13:00", "saturday"),
    ("Mon-Fri, 09:00-11:00", "weekday"),
)

SLOT_LABEL = {key: label for label, key in SLOTS}

# Which slot each course takes. All four AI tiers run every intake (that is
# what keeps the 60-day ladder promise), so they cannot share a slot: one
# facilitator cannot run four rooms at once. Each tier therefore takes its own
# slot, which means a learner climbing the ladder changes evening each tier.
SLOT_FOR = {
    "ai-foundation": "evening-a",
    "ai-practitioner": "evening-b",
    "ai-builder": "saturday",
    "ai-specialist": "weekday",
    "digital-literacy": "weekday",
    "microsoft-office-suite": "weekday",
    "graphic-design": "evening-b",
    "digital-marketing": "evening-b",
    "content-creation": "evening-b",
    "business-growth": "evening-b",
    "financial-sacco": "evening-b",
    "practical-stem": "saturday",
    "scratch-coding": "saturday",
}

# A facilitator runs one room at a time. With four slots in use, an intake that
# carries all four AI tiers plus rotating courses needs more than one person,
# unless low-enrolment courses are dropped first.
FACILITATORS = 2


def first_monday(year: int, month: int) -> date:
    d = date(year, month, 1)
    return d + timedelta(days=(7 - d.weekday()) % 7)


def weeks_of(course: dict) -> int:
    """The leading week count in a duration string, e.g. '6 weeks · 12 sessions'."""
    return int(course["duration"].split("·")[0].strip().split()[0])


@dataclass(frozen=True)
class Sitting:
    course: dict
    start: date
    track: str
    _slot: str | None = None

    @property
    def weeks(self) -> int:
        return weeks_of(self.course)

    @property
    def end(self) -> date:
        # Last session falls on a weekday before the final weekend.
        return self.start + timedelta(weeks=self.weeks - 1, days=4)

    @property
    def enrol_opens(self) -> date:
        return self.start - timedelta(weeks=6)

    @property
    def enrol_closes(self) -> date:
        return self.start - timedelta(days=7)

    @property
    def slot(self) -> str:
        return self._slot or SLOT_FOR.get(self.course["slug"], "weekday")

    @property
    def slot_label(self) -> str:
        return SLOT_LABEL[self.slot]


def build_schedule() -> tuple[list[Sitting], list[dict]]:
    """Four intakes a year, filled to capacity rather than to ambition.

    Capacity is the real constraint: one facilitator runs one room at a time,
    and four slots exist, so one facilitator carries four cohorts per intake.
    The AI ladder is filled first because it is the revenue engine and because
    the 60-day promise depends on the next tier actually running. Whatever
    slots remain go to rotating courses.

    The higher AI tiers only start once a cohort can plausibly exist: AI-201
    from the second intake, AI-301 from the third, AI-401 from the fourth.
    Scheduling AI-401 in the first intake would create a class with no
    graduates to fill it.

    Returns the sittings and a list of deferrals, so the caller can report
    what did not fit instead of silently dropping it.
    """
    by_slug = {c["slug"]: c for c in COURSES}
    capacity = len(SLOTS) * FACILITATORS
    out: list[Sitting] = []
    deferred: list[dict] = []
    intake_index = 0

    for year in YEARS:
        for i, month in enumerate(INTAKE_MONTHS):
            start = first_monday(year, month)
            used = 0

            # The ladder: tier n becomes available from intake n onwards.
            for tier, slug in enumerate(LADDER):
                if intake_index < tier:
                    continue
                if used >= capacity:
                    deferred.append({"course": by_slug[slug], "start": start,
                                     "reason": "no free slot"})
                    continue
                out.append(Sitting(by_slug[slug], start, "ai-ladder"))
                used += 1

            for slug in ROTATION[i]:
                if used >= capacity:
                    deferred.append({"course": by_slug[slug], "start": start,
                                     "reason": "no free slot"})
                    continue
                out.append(Sitting(by_slug[slug], start, "rotating"))
                used += 1

            intake_index += 1

    out.sort(key=lambda s: (s.start, s.course["code"]))
    return out, deferred


def slot_assignments(schedule: list[Sitting]) -> tuple[list[Sitting], list[dict]]:
    """Give each sitting a slot and a room.

    Each course has a preferred slot in SLOT_FOR — Saturday for school-age
    courses, evenings for working adults. A sitting takes its preferred slot
    when a room is free there, and only falls back to another slot when it is
    not. A slot holds one cohort per facilitator.
    """
    out: list[Sitting] = []
    unplaced: list[dict] = []

    by_intake: dict[date, list[Sitting]] = {}
    for s in schedule:
        by_intake.setdefault(s.start, []).append(s)

    slot_order = [key for _, key in SLOTS]

    for start, group in by_intake.items():
        group.sort(key=lambda s: (s.track != "ai-ladder", s.course["code"]))
        free = {key: FACILITATORS for key in slot_order}

        for s in group:
            preferred = SLOT_FOR.get(s.course["slug"], "weekday")
            candidates = [preferred] + [k for k in slot_order if k != preferred]
            chosen = next((k for k in candidates if free[k] > 0), None)
            if chosen is None:
                unplaced.append({"course": s.course, "start": start})
                continue
            free[chosen] -= 1
            out.append(Sitting(s.course, s.start, s.track, _slot=chosen))

    out.sort(key=lambda s: (s.start, s.course["code"]))
    return out, unplaced


def validate() -> list[str]:
    """Every slug must exist, and every course must be scheduled somewhere."""
    known = {c["slug"] for c in COURSES}
    problems = []

    referenced = set(LADDER) | set(ROLLING) | set(SELF_PACED)
    for group in ROTATION:
        referenced |= set(group)

    for slug in sorted(referenced - known):
        problems.append(f"unknown slug in schedule: {slug}")

    covered = referenced | {"ai-foundation"}
    for c in COURSES:
        if c["slug"] not in covered:
            problems.append(f"course not scheduled anywhere: {c['slug']}")

    return problems


def ladder_check(schedule: list[Sitting]) -> list[tuple]:
    """Does every AI-101 finish lead to an AI-201 inside the discount window?

    The final intake of the modelled horizon has no successor inside the
    window, which is an artefact of where the calendar stops rather than a
    scheduling failure. Those rows are returned with gap=None and ok=None so
    callers can report them as "beyond horizon" instead of a breach.
    """
    aif = sorted(
        (s for s in schedule if s.course["slug"] == "ai-foundation"),
        key=lambda s: s.start,
    )
    a2 = sorted(
        (s for s in schedule if s.course["slug"] == "ai-practitioner"),
        key=lambda s: s.start,
    )
    horizon = max(s.start for s in schedule)

    rows = []
    for s in aif:
        later = [n for n in a2 if n.start > s.end]
        if not later:
            beyond = s.start.year == horizon.year and s.start.month == INTAKE_MONTHS[-1]
            rows.append((s, None, None, None if beyond else False))
            continue
        nxt = later[0]
        gap = (nxt.start - s.end).days
        rows.append((s, nxt, gap, gap <= LADDER_WINDOW))
    return rows


# Cost lines from BUSINESS-MANUAL.md 3.1, per cohort of 12.
COHORT_COSTS = {
    "venue": 600_000,
    "internet": 200_000,
    "printing": 250_000,
    "refreshments": 400_000,
    "marketing": 300_000,
}
FACILITATOR_FEE = 1_200_000

# Fees, mirroring the rate card and the manual.
FEE = {
    "ai-foundation": 350_000,
    "ai-practitioner": 550_000,
    "ai-builder": 750_000,
    "ai-specialist": 950_000,
    "digital-literacy": 200_000,
    "graphic-design": 350_000,
    "digital-marketing": 450_000,
    "content-creation": 350_000,
    "business-growth": 450_000,
    "financial-sacco": 400_000,
    "practical-stem": 250_000,
    "scratch-coding": 200_000,
    "microsoft-office-suite": 450_000,
}


def cohort_economics(course: dict, size: int, self_facilitated: bool) -> dict:
    """Revenue and contribution for one cohort, using the manual's cost lines."""
    fee = FEE.get(course["slug"], 350_000)
    revenue = fee * size
    costs = sum(COHORT_COSTS.values())
    if not self_facilitated:
        costs += FACILITATOR_FEE
    return {
        "fee": fee,
        "size": size,
        "revenue": revenue,
        "costs": costs,
        "contribution": revenue - costs,
        "runs": size >= MIN_TO_RUN,
    }


def year_projection(schedule: list[Sitting], size: int, year: int,
                    self_facilitated: bool = True) -> dict:
    """Contribution for one year, counting only cohorts at break-even size."""
    rows = []
    for s in schedule:
        if s.start.year != year:
            continue
        e = cohort_economics(s.course, size, self_facilitated)
        rows.append((s, e))

    run = [r for r in rows if r[1]["runs"]]
    return {
        "year": year,
        "sittings": len(rows),
        "running": len(run),
        "revenue": sum(e["revenue"] for _, e in run),
        "costs": sum(e["costs"] for _, e in run),
        "contribution": sum(e["contribution"] for _, e in run),
        "rows": rows,
    }


def next_intake(today: date) -> date:
    candidates = [first_monday(y, m) for y in YEARS for m in INTAKE_MONTHS]
    future = [c for c in candidates if c >= today]
    return min(future) if future else candidates[-1]


def contact_hours(course: dict) -> int:
    m = re.search(r"(\d+)\s*contact hours", course["duration"])
    return int(m.group(1)) if m else 24


if __name__ == "__main__":
    problems = validate()
    print("validation:", "clean" if not problems else problems)

    schedule, deferred = build_schedule()
    placed, unplaced = slot_assignments(schedule)
    print(f"\n{len(placed)} sittings across {YEARS[0]}-{YEARS[-1]}"
          f"  (deferred {len(deferred)}, unplaced {len(unplaced)})")

    print("\nLadder rule (next tier must start within 60 days of finishing):")
    breaches = 0
    for s, nxt, gap, ok in ladder_check(placed):
        if nxt is None:
            mark = "beyond horizon" if ok is None else "BREACH"
            print(f"  {mark:14s} AI-101 {s.start:%d %b %Y} — no AI-201 in calendar")
            breaches += ok is False
            continue
        breaches += not ok
        print(f"  {'ok  ' if ok else 'BREACH'}  AI-101 {s.start:%d %b %Y}"
              f" ends {s.end:%d %b} -> AI-201 {nxt.start:%d %b} ({gap} days)")
    print(f"  breaches: {breaches}")

    print("\nCapacity:")
    for y in YEARS:
        rows = [s for s in placed if s.start.year == y]
        hrs = sum(contact_hours(s.course) for s in rows)
        print(f"  {y}: {len(rows)} cohorts, {hrs} contact hours,"
              f" {hrs / FACILITATORS:.0f} h per facilitator")

    print("\nProjection (self-facilitated, all cohorts at stated size):")
    for size in (MIN_TO_RUN, MAX_INDIVIDUAL):
        for y in YEARS:
            p = year_projection(placed, size, y)
            print(f"  {y} at {size:2d} learners: revenue {p['revenue']:>12,}"
                  f"  contribution {p['contribution']:>12,}")
