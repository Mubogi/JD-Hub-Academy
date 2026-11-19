"""Checks for the cohort calendar. Run: python3 scripts/test_calendar.py

These exist because the calendar makes a commercial promise — 10 percent off
the next tier within 60 days — and a silent scheduling change could break it
without anyone noticing until a learner asks for the discount.
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from build_calendar import markdown  # noqa: E402
from calendar_plan import (  # noqa: E402
    FACILITATORS,
    MAX_INDIVIDUAL,
    MIN_TO_RUN,
    ROLLING,
    SELF_PACED,
    YEARS,
    build_schedule,
    ladder_check,
    slot_assignments,
    validate,
    year_projection,
)
from catalogue import COURSES  # noqa: E402


def check_ladder_promise(placed) -> list[str]:
    """Every AI-101 must be followed by an AI-201 inside the discount window."""
    out = []
    for s, nxt, gap, ok in ladder_check(placed):
        if ok is not False:
            continue
        if nxt is None:
            out.append(f"ladder breach: AI-101 {s.start} has no AI-201 after it")
        else:
            out.append(
                f"ladder breach: AI-101 {s.start} ends {s.end}, "
                f"next AI-201 {gap} days later"
            )
    return out


def check_capacity(placed) -> list[str]:
    """No slot may hold more cohorts than there are facilitators."""
    counts = Counter((s.start, s.slot) for s in placed)
    return [
        f"slot overload: {start} {slot} has {n} cohorts, limit {FACILITATORS}"
        for (start, slot), n in counts.items()
        if n > FACILITATORS
    ]


def check_coverage(placed) -> list[str]:
    """Every course must be scheduled, rolling, or explicitly self-paced."""
    scheduled = {s.course["slug"] for s in placed} | set(ROLLING) | set(SELF_PACED)
    return [
        f"course has no home: {c['slug']}"
        for c in COURSES
        if c["slug"] not in scheduled
    ]


def check_dates(placed) -> list[str]:
    problems = []
    for s in placed:
        if s.end <= s.start:
            problems.append(f"ends before it starts: {s.course['code']} {s.start}")
        if s.enrol_closes >= s.start:
            problems.append(f"enrolment closes after start: {s.course['code']}")
        if s.enrol_opens >= s.enrol_closes:
            problems.append(f"enrolment window inverted: {s.course['code']}")
    return problems


def check_economics(placed) -> list[str]:
    problems = []
    for size in (MIN_TO_RUN, MAX_INDIVIDUAL):
        for year in YEARS:
            p = year_projection(placed, size, year)
            if p["contribution"] < 0:
                problems.append(
                    f"negative contribution: {year} at {size} learners "
                    f"({p['contribution']:,})"
                )
    return problems


def check_determinism(placed) -> list[str]:
    if markdown(placed) != markdown(placed):
        return ["markdown output is not deterministic"]
    return []


def main() -> int:
    schedule, deferred = build_schedule()
    placed, unplaced = slot_assignments(schedule)

    failures = list(validate())
    failures += [f"deferred with no reason: {d}" for d in deferred]
    failures += [f"unplaced: {u['course']['code']} {u['start']}" for u in unplaced]
    failures += check_ladder_promise(placed)
    failures += check_capacity(placed)
    failures += check_coverage(placed)
    failures += check_dates(placed)
    failures += check_economics(placed)
    failures += check_determinism(placed)

    ladder = len([s for s in placed if s.track == "ai-ladder"])
    print(f"{len(placed)} sittings, {ladder} on the AI ladder")

    if failures:
        print(f"\n{len(failures)} failure(s):")
        for f in failures:
            print("  -", f)
        return 1

    print("all checks pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
