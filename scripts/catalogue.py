"""The JD Hub Academy course catalogue.

One entry per course. Everything else — covers, illustrations, the catalogue
index, and the PDF books — is generated from this list, so adding a course
means adding one dict here and writing its Markdown source.

`tier` drives the "come back and upgrade" ladder: a learner finishes a
Foundation course, returns for Practitioner, then Builder, then Specialist.
Courses without tiers are single-book courses.
"""

from __future__ import annotations

COURSES = [
    # ------------------------------------------------------------------
    # FLAGSHIP BOOK — leadership
    # ------------------------------------------------------------------
    {
        "code": "LD-001",
        "slug": "leadership",
        "title": "From Scratch to President",
        "subtitle": "Principles and daily tasks for building a life of consequence",
        "category": "financials",
        "tier": "",
        "level": "Everyone — the book to read first and re-read every year",
        "duration": "52 weeks · one principle and one task per week",
        "icon": "growth",
        "summary": (
            "A year-long manual for building something from nothing. Fifty-two weekly "
            "principles, each with a task you can complete in a day, drawn from the "
            "actual work of building businesses, systems and institutions. Not "
            "motivation. Mechanics, with Scripture as the foundation."
        ),
        "outcomes": [
            "Build the habits that precede any result worth having",
            "Price your work, your time and your standards",
            "Build systems that run without your presence",
            "Lead people without manipulating them",
            "Handle money, debt and growth without losing the business",
            "Make decisions under uncertainty and live with them",
            "Leave something that outlives your involvement",
        ],
        "prereqs": "Honesty about where you currently are.",
        "audience": "Founders, students, pastors, civil servants, tradespeople, parents.",
        "next": "Business Growth & Sales Systems, then AI-201",
    },
    # ------------------------------------------------------------------
    # FLAGSHIP — Artificial Intelligence
    # ------------------------------------------------------------------
    {
        "code": "AI-101",
        "slug": "ai-foundation",
        "title": "AI in Everyday Life & Business",
        "subtitle": "Foundation: use AI confidently, safely, and every single day",
        "category": "ai",
        "tier": "Foundation",
        "level": "Beginner — no prior AI knowledge",
        "duration": "6 weeks · 12 sessions · 24 contact hours",
        "icon": "spark",
        "summary": (
            "The starting point for anyone who has been told to 'learn AI' and given "
            "no instructions. You will use ChatGPT, Google Gemini, Meta AI and Canva "
            "on your own real work — not on sample exercises — and leave with a "
            "personal AI workflow you actually use."
        ),
        "outcomes": [
            "Explain what generative AI is, and the three ways it fails",
            "Write prompts that get usable answers on the first or second try",
            "Run ChatGPT, Gemini and Meta AI confidently for daily work",
            "Produce a week of social content in under an hour",
            "Draft business documents in a fraction of the usual time",
            "Verify AI output and spot invented facts",
            "Apply a personal and business AI policy",
        ],
        "prereqs": "A smartphone or laptop, a Google account, WhatsApp, and basic typing.",
        "audience": "Small business owners, employees, job seekers, students, NGO staff.",
        "next": "AI-201 Practitioner",
    },
    {
        "code": "AI-201",
        "slug": "ai-practitioner",
        "title": "AI Practitioner",
        "subtitle": "Turn AI from a toy into a working system for your job or business",
        "category": "ai",
        "tier": "Practitioner",
        "level": "Intermediate — AI-101 or equivalent confidence",
        "duration": "8 weeks · 16 sessions · 32 contact hours",
        "icon": "circuit",
        "summary": (
            "You already use AI. Now you build systems with it. This tier covers "
            "prompt architecture, reusable prompt libraries, AI-assisted research "
            "you can defend, document intelligence, content engines, and simple "
            "automation that runs without you."
        ),
        "outcomes": [
            "Design multi-step prompt chains that hold quality across a team",
            "Build and maintain a shared prompt library for an organisation",
            "Interrogate long documents with NotebookLM and defend your findings",
            "Run a repeatable weekly content engine across four platforms",
            "Automate recurring admin with Zapier or Make",
            "Measure time and cost saved, with evidence",
        ],
        "prereqs": "AI-101, or six months of regular AI use.",
        "audience": "Supervisors, administrators, marketers, teachers, founders.",
        "next": "AI-301 Builder",
    },
    {
        "code": "AI-301",
        "slug": "ai-builder",
        "title": "AI Builder",
        "subtitle": "Custom assistants, image pipelines, and no-code agents",
        "category": "ai",
        "tier": "Builder",
        "level": "Advanced — comfortable with systems and data",
        "duration": "8 weeks · 16 sessions · 32 contact hours",
        "icon": "blocks",
        "summary": (
            "Build things other people use. Custom GPTs and Gemini Gems trained on "
            "your own documents, brand-consistent image generation pipelines, "
            "voice and video production, retrieval over your own knowledge base, "
            "and agents that take actions rather than just answering."
        ),
        "outcomes": [
            "Build a custom assistant grounded in your organisation's documents",
            "Design a brand-locked image generation system",
            "Produce voiceover and short video with AI, legally and consistently",
            "Build retrieval-augmented assistants and test them for hallucination",
            "Deploy a customer-facing bot with escalation rules",
            "Design an agent that takes actions safely",
        ],
        "prereqs": "AI-201, or proven experience shipping an AI workflow.",
        "audience": "Operations leads, product owners, in-house tech staff, consultants.",
        "next": "AI-401 Specialist",
    },
    {
        "code": "AI-401",
        "slug": "ai-specialist",
        "title": "AI Specialist & Advisor",
        "subtitle": "Governance, evaluation, and selling AI work to organisations",
        "category": "ai",
        "tier": "Specialist",
        "level": "Professional — for consultants and organisational leads",
        "duration": "6 weeks · 12 sessions · 24 contact hours",
        "icon": "shield",
        "summary": (
            "The tier that turns skill into income and authority. AI governance and "
            "policy, model evaluation, procurement, data protection, staff training "
            "design, and the commercial side: scoping, pricing and delivering AI "
            "consulting engagements."
        ),
        "outcomes": [
            "Write and roll out an organisational AI policy that survives audit",
            "Evaluate and compare AI tools on evidence, not marketing",
            "Assess risk, data protection and compliance obligations",
            "Design and deliver AI training for staff at three skill levels",
            "Scope, price and deliver an AI consulting engagement",
            "Build a defensible AI service offering and price it",
        ],
        "prereqs": "AI-301, or equivalent delivery experience.",
        "audience": "Consultants, IT managers, compliance officers, trainers, founders.",
        "next": "Alumni network & specialist clinics",
    },
    # ------------------------------------------------------------------
    # SITE CATALOGUE — the eleven other courses
    # ------------------------------------------------------------------
    {
        "code": "SW-110",
        "slug": "scratch-coding",
        "title": "Scratch Coding",
        "subtitle": "Block-based programming for the Uganda and Cambridge curricula",
        "category": "stem",
        "tier": "",
        "level": "Beginner — ages 8 and up",
        "duration": "8 weeks · 16 sessions · 24 contact hours",
        "icon": "blocks",
        "summary": (
            "Children build animations, games and interactive stories while learning "
            "computational thinking. Every lesson maps to a named competency in the "
            "Uganda lower-secondary ICT syllabus and the Cambridge Primary/Secondary "
            "Computing framework, so parents can see the progress."
        ),
        "outcomes": [
            "Sequence, loop, and use events to control sprites",
            "Apply conditionals, variables and operators",
            "Design and debug a multi-level game",
            "Build an interactive story with broadcast messaging",
            "Present a finished project and explain the logic",
        ],
        "prereqs": "Basic reading and mouse or touchscreen control.",
        "audience": "Children 8–16, and teachers who want to deliver the curriculum.",
        "next": "Practical STEM, then Python foundations",
    },
    {
        "code": "SW-120",
        "slug": "digital-literacy",
        "title": "Basic Digital Literacy",
        "subtitle": "From switching on to working online, safely",
        "category": "software",
        "tier": "",
        "level": "Beginner — no computer experience assumed",
        "duration": "4 weeks · 8 sessions · 16 contact hours",
        "icon": "laptop",
        "summary": (
            "The course for adults who have been handed a computer and expected to "
            "know what to do. No assumptions, no jargon, and no shame. By the end "
            "you can file, email, search, pay, and protect yourself online."
        ),
        "outcomes": [
            "Operate a computer, phone, and file system without help",
            "Create, save, find and share documents",
            "Use email and WhatsApp for work correspondence",
            "Search effectively and judge whether a source is trustworthy",
            "Recognise scams, phishing, and mobile-money fraud",
            "Complete a task end-to-end: apply, register, or pay online",
        ],
        "prereqs": "None. Literally none.",
        "audience": "Adult learners, market traders, community leaders, new staff.",
        "next": "Microsoft Word, then AI-101",
    },
    {
        "code": "ST-130",
        "slug": "practical-stem",
        "title": "Practical STEM",
        "subtitle": "Electronics, robotics and real experiments with real materials",
        "category": "stem",
        "tier": "",
        "level": "Beginner to Intermediate",
        "duration": "10 weeks · 20 sessions · 30 contact hours",
        "icon": "flask",
        "summary": (
            "Science you can hold. Learners wire circuits, build a working robot from "
            "a block kit, and run inquiry experiments using cheap local materials — "
            "then model the results in a spreadsheet. Designed for schools without a "
            "laboratory budget."
        ),
        "outcomes": [
            "Apply the scientific method to a question you chose",
            "Build and fault-find series and parallel circuits",
            "Program a block-based robot to complete a task",
            "Collect, tabulate and graph real measurements",
            "Present findings as a scientific poster",
        ],
        "prereqs": "Basic numeracy. Curiosity required.",
        "audience": "Ages 10–18, teachers, and school science clubs.",
        "next": "Scratch Coding, then electronics at AI-301 level",
    },
    {
        "code": "DS-140",
        "slug": "graphic-design",
        "title": "Graphic Design",
        "subtitle": "Canva, InShot and the AI tools that changed the job",
        "category": "design",
        "tier": "",
        "level": "Beginner to Intermediate",
        "duration": "6 weeks · 12 sessions · 24 contact hours",
        "icon": "pen",
        "summary": (
            "Design that earns money. Brand identity, typography, colour, posters, "
            "social graphics, and short-form video — taught on Canva and InShot, with "
            "the current AI generation and editing tools built in. Ends with a "
            "portfolio and a price list."
        ),
        "outcomes": [
            "Apply hierarchy, contrast, alignment and the three-colour rule",
            "Build a brand kit: logo, palette, type, templates",
            "Design print-ready posters and social graphics",
            "Edit short-form video with captions and transitions",
            "Use AI generation and background removal without breaking the brand",
            "Price and quote design work confidently",
        ],
        "prereqs": "Basic phone or computer use.",
        "audience": "Aspiring freelancers, church and NGO media teams, shop owners.",
        "next": "AI-201, for AI-assisted content at scale",
    },
    {
        "code": "FN-150",
        "slug": "financial-sacco",
        "title": "Financial & SACCO Management",
        "subtitle": "Bookkeeping, savings cycles, loans and portfolio quality",
        "category": "financials",
        "tier": "",
        "level": "Intermediate",
        "duration": "6 weeks · 12 sessions · 24 contact hours",
        "icon": "chart",
        "summary": (
            "How money actually moves through a SACCO or small business, and how to "
            "keep records that survive an audit. Double-entry bookkeeping, savings and "
            "loan cycles, arrears management, and the reports a board actually reads — "
            "with the JD Hub SACCO system used throughout."
        ),
        "outcomes": [
            "Record transactions using double-entry bookkeeping",
            "Run a savings and loan cycle from opening to closing",
            "Calculate and interpret portfolio quality indicators",
            "Manage arrears before they become losses",
            "Prepare monthly reports a board can act on",
            "Apply the regulatory basics for Ugandan SACCOs",
        ],
        "prereqs": "Basic numeracy and spreadsheet familiarity.",
        "audience": "SACCO staff and board members, treasurers, SME owners.",
        "next": "Microsoft Excel, for financial modelling",
    },
    {
        "code": "MS-160",
        "slug": "microsoft-word",
        "title": "Microsoft Word",
        "subtitle": "Documents that look professional and behave predictably",
        "category": "software",
        "tier": "",
        "level": "Beginner to Intermediate",
        "duration": "2 weeks · 8 sessions · 12 contact hours",
        "icon": "word",
        "summary": (
            "Most people use ten percent of Word and fight the other ninety. This "
            "course fixes that: styles, sections, tables, mail merge, and long "
            "documents that do not fall apart when you add a page."
        ),
        "outcomes": [
            "Apply styles so formatting is consistent and changeable in one click",
            "Build tables, columns and multi-section layouts",
            "Use mail merge for letters, certificates and labels",
            "Create an automatic table of contents and page numbering",
            "Track changes and review a document collaboratively",
            "Produce a print-ready report, CV and certificate",
        ],
        "prereqs": "Basic typing and file handling.",
        "audience": "Office staff, administrators, students, teachers, job seekers.",
        "next": "Microsoft Excel",
    },
    {
        "code": "MS-170",
        "slug": "microsoft-excel",
        "title": "Microsoft Excel",
        "subtitle": "From a list of numbers to a decision",
        "category": "software",
        "tier": "",
        "level": "Beginner to Intermediate",
        "duration": "2 weeks · 8 sessions · 12 contact hours",
        "icon": "excel",
        "summary": (
            "Formulas that work, lookups that do not break, pivot tables that answer "
            "questions, and dashboards someone else can read. Includes the AI "
            "features now built into Excel and Sheets."
        ),
        "outcomes": [
            "Write formulas with confidence and debug them methodically",
            "Use VLOOKUP/XLOOKUP, INDEX-MATCH and conditional logic",
            "Clean messy data and remove duplicates safely",
            "Build pivot tables and a one-page dashboard",
            "Apply conditional formatting that highlights what matters",
            "Automate a recurring report",
        ],
        "prereqs": "Basic computer use. No maths beyond arithmetic.",
        "audience": "Administrators, accountants, shop owners, researchers.",
        "next": "Microsoft Access, or Financial & SACCO Management",
    },
    {
        "code": "MS-180",
        "slug": "microsoft-powerpoint",
        "title": "Microsoft PowerPoint",
        "subtitle": "Presentations people actually remember",
        "category": "software",
        "tier": "",
        "level": "Beginner to Intermediate",
        "duration": "2 weeks · 8 sessions · 12 contact hours",
        "icon": "powerpoint",
        "summary": (
            "Design, structure and delivery. Slide masters, restraint in animation, "
            "charts that make one point, and the rehearsal habits that separate a "
            "confident presenter from a nervous one."
        ),
        "outcomes": [
            "Build a slide master and a reusable template",
            "Structure a presentation around one argument",
            "Design charts that make a single point legible",
            "Use animation and transitions without embarrassing yourself",
            "Rehearse with presenter tools and timing",
            "Export to video and PDF for distribution",
        ],
        "prereqs": "Basic computer use.",
        "audience": "Students, teachers, business presenters, church leaders.",
        "next": "Graphic Design, for visual polish",
    },
    {
        "code": "MS-190",
        "slug": "microsoft-access",
        "title": "Microsoft Access",
        "subtitle": "Build a working database application without writing code",
        "category": "software",
        "tier": "",
        "level": "Intermediate to Advanced",
        "duration": "2 weeks · 8 sessions · 12 contact hours",
        "icon": "database",
        "summary": (
            "When Excel stops coping. Table design, relationships, queries, forms and "
            "reports — ending with a small working application for members, stock or "
            "clients, complete with a navigation menu."
        ),
        "outcomes": [
            "Normalise data and design tables properly",
            "Build relationships with referential integrity",
            "Write select, parameter and action queries",
            "Build data-entry forms with validation",
            "Produce grouped reports and print layouts",
            "Assemble a navigation system with macros",
        ],
        "prereqs": "Microsoft Excel, or equivalent comfort with data.",
        "audience": "Records officers, registrars, stock controllers, clinic staff.",
        "next": "AI-201, for querying data in plain language",
    },
    {
        "code": "MS-195",
        "slug": "word-excel-combo",
        "title": "Microsoft Word + Excel Combo",
        "subtitle": "The office pair that does ninety percent of real work",
        "category": "software",
        "tier": "",
        "level": "Beginner to Intermediate",
        "duration": "2 weeks · 8 sessions · 12 contact hours",
        "icon": "wordexcel",
        "summary": (
            "Word and Excel taught together, because that is how work actually "
            "arrives. Documents with live tables, mail merge from a spreadsheet, and "
            "reports where the numbers update themselves."
        ),
        "outcomes": [
            "Format professional documents with styles",
            "Build tables, images and mail merge in Word",
            "Enter, format and calculate in Excel",
            "Use lookups, charts and pivot tables",
            "Link Excel data into a Word document",
            "Deliver a report with an embedded live spreadsheet",
        ],
        "prereqs": "Basic typing and file handling.",
        "audience": "Office staff, administrators, students, small business owners.",
        "next": "Microsoft Office Suite (All Tools)",
    },
    {
        "code": "DS-210",
        "slug": "content-creation",
        "title": "Content Creation & Storytelling",
        "subtitle": "Make the video, the photo, the poster and the story that sells",
        "category": "design",
        "tier": "",
        "level": "Beginner to Intermediate",
        "duration": "6 weeks · 12 sessions · 24 contact hours",
        "icon": "camera",
        "summary": (
            "A phone is enough. This course turns a learner into a producer: shooting "
            "clean video on a cheap handset, recording usable audio in a noisy room, "
            "editing with CapCut, writing scripts that hold attention, and using "
            "current AI video, image and voice tools without producing the same "
            "soulless output as everyone else."
        ),
        "outcomes": [
            "Shoot video on a phone that looks deliberate, not accidental",
            "Record clean audio in a noisy environment",
            "Write a 30-second script with a hook, a point and a call to action",
            "Edit to a finished cut with captions, music and b-roll",
            "Use AI for voiceover, image and video generation responsibly",
            "Build a content series that people return to",
            "Publish consistently without burning out",
        ],
        "prereqs": "A smartphone with a camera. That is the whole kit list.",
        "audience": "Creators, church media teams, NGO communicators, small brands.",
        "next": "Digital Marketing & Business Growth",
    },
    {
        "code": "MK-220",
        "slug": "digital-marketing",
        "title": "Digital Marketing",
        "subtitle": "Get found, get chosen, get paid — with a budget you can afford",
        "category": "design",
        "tier": "",
        "level": "Beginner to Intermediate",
        "duration": "8 weeks · 16 sessions · 32 contact hours",
        "icon": "megaphone",
        "summary": (
            "Marketing taught as arithmetic, not magic. Who your buyer is, where they "
            "already are, what makes them choose you, and how to spend the smallest "
            "possible amount of money finding out. Covers WhatsApp Business, Facebook "
            "and Instagram ads, Google Business Profile, TikTok, email and the "
            "AI tools that cut production cost to near zero."
        ),
        "outcomes": [
            "Define a buyer and a positioning statement you can defend",
            "Set up WhatsApp Business, a Google Business Profile and a Facebook page properly",
            "Run a small paid campaign and read the results honestly",
            "Write an offer that converts without discounting to death",
            "Build a simple funnel and measure where it leaks",
            "Calculate cost per lead and cost per sale",
            "Decide when to spend more and when to stop",
        ],
        "prereqs": "Basic smartphone use. A business, cause or service to market.",
        "audience": "Business owners, marketers, freelancers, NGO programme staff.",
        "next": "Business Growth & Sales Systems",
    },
    {
        "code": "BZ-230",
        "slug": "business-growth",
        "title": "Business Growth & Sales Systems",
        "subtitle": "From hustling to a business that runs without you in the room",
        "category": "financials",
        "tier": "",
        "level": "Intermediate",
        "duration": "8 weeks · 16 sessions · 32 contact hours",
        "icon": "growth",
        "summary": (
            "The gap between a hustle and a business is systems. Pricing that protects "
            "your margin, a sales process that does not depend on charm, customer "
            "retention that costs less than acquisition, and the numbers a founder "
            "must know every week. Heavy on templates, light on theory."
        ),
        "outcomes": [
            "Price a product or service using cost, value and market logic",
            "Build a repeatable sales process from enquiry to repeat purchase",
            "Track the five numbers that predict survival",
            "Design a customer retention and referral system",
            "Document a process so staff can run it without you",
            "Decide whether to grow, hold, or exit",
            "Write a one-page growth plan a lender would read",
        ],
        "prereqs": "An operating business, side hustle, or firm intention to start one.",
        "audience": "Founders, shop owners, service providers, SACCO entrepreneurs.",
        "next": "Financial & SACCO Management, or AI-201",
    },
    {
        "code": "MS-200",
        "slug": "microsoft-office-suite",
        "title": "Microsoft Office Suite (All Tools)",
        "subtitle": "Word, Excel, PowerPoint, Access and Outlook as one system",
        "category": "software",
        "tier": "",
        "level": "Beginner to Advanced",
        "duration": "4 weeks · 16 sessions · 24 contact hours",
        "icon": "suite",
        "summary": (
            "The complete office productivity programme. Each tool to working "
            "competence, then the part nobody teaches: making them work together, "
            "with a capstone project that uses all five."
        ),
        "outcomes": [
            "Produce professional documents, spreadsheets and presentations",
            "Design a small database and report from it",
            "Manage email, calendar and contacts in Outlook",
            "Link tools: Excel to Word, Access to Excel, data to slides",
            "Deliver a capstone project spanning the suite",
            "Sit an employer-recognised practical assessment",
        ],
        "prereqs": "Basic computer use.",
        "audience": "Job seekers, office staff, administrators, graduates.",
        "next": "AI-101, to add AI to the workflow",
    },
]


def by_slug(slug: str) -> dict:
    for c in COURSES:
        if c["slug"] == slug:
            return c
    raise KeyError(slug)


def ai_ladder() -> list[dict]:
    return [c for c in COURSES if c["category"] == "ai"]
